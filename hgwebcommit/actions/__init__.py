from hgwebcommit.actions.base import InvalidAction, BaseAction, FunctionAction, ActionManager
from hgwebcommit.actions.command import ExecuteCommandAction
from hgwebcommit.actions.commit import CommitAction
from hgwebcommit.actions.loaders import ActionLoader

manager = ActionManager()
loader = ActionLoader()
