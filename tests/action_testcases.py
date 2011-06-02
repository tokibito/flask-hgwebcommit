# coding:utf8
from unittest import TestCase

from hgwebcommit.actions import FunctionAction, ActionManager

__all__ = ['ActionTestCase', 'ActionManagerTestCase']

class ActionTestCase(TestCase):
    """
    Actionのテスト
    """
    def test_call(self):
        action = FunctionAction('test', 'test', lambda :'ok')
        self.assertEqual(action(), 'ok')

class ActionManagerTestCase(TestCase):
    """
    ActionManagerのテスト
    """
    def setUp(self):
        self.action = FunctionAction('test', 'test', lambda :'ok')
        self.manager = ActionManager()

    def test_add(self):
        self.manager.add(self.action)
        self.assertEqual(len(self.manager.actions), 1)

    def test_call(self):
        self.manager.add(self.action)
        self.assertEqual(self.manager.call('test'), 'ok')
