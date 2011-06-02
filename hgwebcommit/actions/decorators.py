from hgwebcommit.actions import FunctionAction, manager

def action(name, label, params=None):
    def _wrap(func):
        obj = FunctionAction(name, label, func, params)
        manager.add(obj)
        return func
    return _wrap
