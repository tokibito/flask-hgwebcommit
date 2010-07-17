# coding:utf8
import os
import logging
from copy import copy

from werkzeug import MultiDict
from flask import Flask, render_template, request, abort, redirect, url_for, session, flash

from hgwebcommit import app
from hgwebcommit.hgwrapper import MercurialWrapper
from hgwebcommit.forms import SelectFileForm, SelectFileConfirmForm, SelectFileSubmitConfirmForm

# const
OPERATION_MESSAGE = {
  'commit': u'コミットします(commit)',
  'revert': u'戻します(revert)',
  'remove': u'削除します(remove)',
}

# util
def get_repo():
    return MercurialWrapper(app.config['HGWEBCOMMIT_REPOSITORY'], app.config['HGWEBCOMMIT_ENCODING'])

def get_choices_ctrl(repo):
    return [(val, 'M %s' % val) for val in repo.status_modified()] + \
        [(val, 'A %s' % val) for val in repo.status_added()] + \
        [(val, 'R %s' % val) for val in repo.status_removed()] + \
        [(val, '! %s' % val) for val in repo.status_deleted()]

def get_choices_unknown(repo):
    return [(val, '? %s' % val) for val in repo.status_unknown()]

def operation_repo(repo, operation, files, commit_message=None):
    if operation == 'commit':
        # コミット
        repo.commit(files, commit_message)
        return u'コミットしました。'
    elif operation == 'revert':
        # 元に戻す
        repo.revert(files)
        return u'元に戻しました。'
    elif operation == 'remove':
        # 削除しました
        repo.remove(files)
        return u'削除しました。'
    else:
        abort(400)

# entry points
@app.route('/')
def index():
    repo = get_repo()
    form_ctrl = SelectFileForm(request.form, prefix='ctrl-')
    form_unknown = SelectFileForm(request.form)
    form_ctrl.files.choices = get_choices_ctrl(repo)
    form_unknown.files.choices = get_choices_unknown(repo)
    return render_template('index.html',
        repository=repo, form_unknown=form_unknown, form_ctrl=form_ctrl)

@app.route('/add_unknown', methods=['POST'])
def add_unknown_confirm():
    """
    管理外のファイル
    """
    repo = get_repo()
    form = SelectFileConfirmForm(request.form)
    form.files.choices = get_choices_unknown(repo)
    if not form.validate():
        abort(400)
    if form.data.get('confirm'):
        # リポジトリに追加
        repo.add(form.data['files'])
        flash(u'追加しました。')
        return redirect(url_for('index'))
    formdata = MultiDict(request.form)
    del formdata['csrf']
    form = SelectFileConfirmForm(None, confirm=1, **formdata)
    form.files.choices = get_choices_unknown(repo)
    form.validate()
    return render_template('add_unknown_confirm.html',
        repository=repo, form=form)

@app.route('/submit', methods=['POST'])
def submit_confirm():
    """
    管理下のファイル
    """
    repo = get_repo()
    form = SelectFileSubmitConfirmForm(request.form, prefix='ctrl-')
    form.files.choices = get_choices_ctrl(repo)
    if not form.validate():
        abort(400)
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
        enable_commit_message=form.data['operation'] == 'commit'
    )
