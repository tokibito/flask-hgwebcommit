from flask import flash
from flaskext.babel import gettext, lazy_gettext

from hgwebcommit.actions.decorators import action

@action('hello', lazy_gettext('Hello'))
def hello():
    flash(gettext('Hello!'))
