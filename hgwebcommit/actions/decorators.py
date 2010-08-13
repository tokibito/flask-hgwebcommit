from hgwebcommit.actions import Action, manager

def action(name, label, params=None):
    def _wrap(func):
        obj = Action(name, label, func, params)
        manager.add(obj)
        return func
    return _wrap
