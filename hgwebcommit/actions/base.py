# coding:utf8
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
        アクションが未ロードならロードする
        """
        if not self.loaded:
            self.loaded = True
            from hgwebcommit.actions import loader
            loader.load_actions()
        return self._actions

    def add(self, action):
        """
        追加
        """
        self._actions.append(action)

    def list(self):
        """
        一覧表示
        (name, label)
        の形式choicesで使う
        """
        return [(action.name, aciton.label) for action in self.actions]

    def pick(self, name):
        """
        名前でアクションを探して返す
        """
        for action in self.actions:
            if action.name == name:
                return action
        raise InvalidAction('No such action "%s"' % name)

    def call(self, name, *args, **kwargs):
        """
        名前を指定してアクションを呼び出す
        """
        action = self.pick(name)
        return action(*args, **kwargs)
