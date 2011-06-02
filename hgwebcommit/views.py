import os
import socket
import logging
from copy import copy

from werkzeug import MultiDict
from flask import Flask, render_template, request, abort, redirect, url_for, session, flash
from flaskext.babel import gettext as _
from flaskext.babel import lazy_gettext

from hgwebcommit import app
#from hgwebcommit.hgwrapper import MercurialWrapper
from hgwebcommit.forms import SelectFileForm, SelectFileConfirmForm, SelectFileSubmitConfirmForm, SelectActionForm
from hgwebcommit.actions import manager as action_manager

# const
OPERATION_MESSAGE = {
  'commit': lazy_gettext('Commit'),
  'revert': lazy_gettext('Revert'),
  'remove': lazy_gettext('Remove'),
}

# util
def get_repo():
    from hgwebcommit.repository import get_repository
    return get_repository(path=app.config['HGWEBCOMMIT_REPOSITORY'], encoding=app.config['HGWEBCOMMIT_ENCODING'])

def get_allow_commit():
    return app.config.get('HGWEBCOMMIT_ALLOW_COMMIT', True)

def get_choices_ctrl(repo):
    return [(val, 'M %s' % val) for val in repo.status_modified()] + \
        [(val, 'A %s' % val) for val in repo.status_added()] + \
        [(val, 'R %s' % val) for val in repo.status_removed()] + \
        [(val, '! %s' % val) for val in repo.status_deleted()]

def get_choices_unknown(repo):
    return [(val, '? %s' % val) for val in repo.status_unknown()]

def operation_repo(repo, operation, files, commit_message=None):
    if operation == 'commit':
        # commit
        repo.commit(files, commit_message)
        app.logger.info('commit - %s [%s]' % (commit_message, ', '.join(files)))
        return _('commited.')
    elif operation == 'revert':
        # revert
        repo.revert(files)
        app.logger.info('reverted - [%s]' % ', '.join(files))
        return _('reverted.')
    elif operation == 'remove':
        # remove
        repo.remove(files)
        app.logger.info('removed - [%s]' % ', '.join(files))
        return _('removed.')
    else:
        abort(400)

def gethostname():
    return socket.gethostname()

# entry points
@app.route('/')
def index():
    """
    top page
    """
    repo = get_repo()
    form_ctrl = SelectFileForm(request.form, prefix='ctrl-')
    form_unknown = SelectFileForm(request.form)
    form_ctrl.files.choices = get_choices_ctrl(repo)
    form_unknown.files.choices = get_choices_unknown(repo)
    form_actions = SelectActionForm(request.form, prefix='action-')
    form_actions.action.choices = action_manager.list()
    return render_template('index.html',
        repository=repo,
        form_unknown=form_unknown,
        form_ctrl=form_ctrl,
        form_actions=form_actions,
        hostname=gethostname(),
        allow_commit=get_allow_commit(),
    )

@app.route('/add_unknown', methods=['POST'])
def add_unknown_confirm():
    """
    Show confirm on adding untracked files
    """
    if not get_allow_commit():
        abort(401)
    repo = get_repo()
    form = SelectFileConfirmForm(request.form)
    form.files.choices = get_choices_unknown(repo)
    if not form.validate():
        flash(_('Invalid request. Please input again.'))
        return redirect(url_for('index'))
    if form.data.get('confirm'):
        # add to repos
        repo.add(form.data['files'])
        flash(_('added.'))
        return redirect(url_for('index'))
    formdata = MultiDict(request.form)
    del formdata['csrf']
    form = SelectFileConfirmForm(None, confirm=1, **formdata)
    form.files.choices = get_choices_unknown(repo)
    form.validate()
    return render_template('add_unknown_confirm.html',
        repository=repo,
        form=form,
        hostname=gethostname(),
    )

@app.route('/submit', methods=['POST'])
def submit_confirm():
    """
    Show confirm submitting
    """
    if not get_allow_commit():
        abort(401)
    repo = get_repo()
    form = SelectFileSubmitConfirmForm(request.form, prefix='ctrl-')
    form.files.choices = get_choices_ctrl(repo)
    if not form.validate():
        flash(_('Invalid request. Please input again.'))
        return redirect(url_for('index'))
    if form.data.get('confirm'):
        # operation
        message = operation_repo(repo, form.data['operation'], form.data['files'], form.data['commit_message'])
        flash(message)
        return redirect(url_for('index'))
    formdata = MultiDict(request.form)
    del formdata['ctrl-csrf']
    form = SelectFileSubmitConfirmForm(None, prefix='ctrl-', confirm=1, **formdata)
    form.files.choices = get_choices_ctrl(repo)
    form.validate()
    return render_template('submit.html',
        repository=repo,
        form=form,
        message=OPERATION_MESSAGE.get(form.data['operation']),
        enable_commit_message=form.data['operation'] == 'commit',
        hostname=gethostname(),
    )

@app.route('/exec_action', methods=['POST'])
def exec_action():
    """
    Run action method
    """
    form = SelectActionForm(request.form, prefix='action-')
    form.action.choices = action_manager.list()
    if form.validate():
        response = action_manager.call(form.data['action'])
        if response is not None:
            return response
    return redirect(url_for('index'))
