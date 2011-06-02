# coding: utf-8
from flask import render_template, request, redirect, url_for, flash
from flaskext.babel import gettext

from hgwebcommit import app
from hgwebcommit.actions.base import BaseAction
from hgwebcommit.utils import exec_command, get_repo
from hgwebcommit.forms import ConfirmForm

class ExecuteCommandAction(BaseAction):
    """
    execute shell command action
    """
    def __init__(self, name, label, command, encoding=None, params=None):
        super(ExecuteCommandAction, self).__init__(name, label, params)
        self.command = command
        self.encoding = encoding or 'utf-8'

    def run(self, *args, **kwargs):
        repo = get_repo()
        form = ConfirmForm(request.form, prefix='action-', csrf_enabled=False)
        if form.validate():
            output = exec_command(self.command)
            app.logger.info('exec_command - %s [%s]' % (self.name, ' '.join(self.command)))
            if self.encoding:
                output = output.decode(self.encoding)
            if output:
                flash_message = output
            else:
                flash_message = gettext('"%(label)s" was executed.', label=self.label)
            flash(flash_message)
            return
        message = gettext('Execute "%(label)s"', label=self.label)
        form = ConfirmForm(None, confirm=1, prefix='action-', csrf_enabled=False)
        return render_template('actions/command.html',
            message=message,
            repository=repo,
            form=form,
        )
