# coding:utf-8
from werkzeug import import_string

from hgwebcommit import app

class ActionLoader(object):
    def load_actions(self):
        action_modules = app.config.get('HGWEBCOMMIT_ACTIONS') or []
        for mod_name in action_modules:
            mod = import_string(mod_name)
