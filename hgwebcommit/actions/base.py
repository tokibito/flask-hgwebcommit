class InvalidAction(Exception):
    pass

class Action(object):
    def __init__(self, name, label, func, params=None):
        self.name = name
        self.label = label
        self.func = func
        self.params = params

    def __call__(self, *args, **kwargs):
        if self.params:
            kwargs.update(self.params)
        return self.func(*args, **kwargs)

class ActionManager(object):
    def __init__(self):
        self._actions = []
        self.loaded = False

    @property
    def actions(self):
        """
        proxy access to actions property
        """
        if not self.loaded:
            self.loaded = True
            from hgwebcommit.actions import loader
            loader.load_actions()
        return self._actions

    def add(self, action):
        """
        add action
        """
        self._actions.append(action)

    def list(self):
        """
        list actions
        result: (name, label)
        eg: use choices.
        """
        return [(action.name, action.label) for action in self.actions]

    def pick(self, name):
        """
        return action by name
        """
        for action in self.actions:
            if action.name == name:
                return action
        raise InvalidAction('No such action "%s"' % name)

    def call(self, name, *args, **kwargs):
        """
        call action by name
        """
        action = self.pick(name)
        return action(*args, **kwargs)
