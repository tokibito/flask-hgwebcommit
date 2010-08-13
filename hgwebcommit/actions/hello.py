# coding:utf8
from flask import flash

from hgwebcommit.actions.decorators import action

@action('hello', u'こんにちは')
def hello():
    flash(u'こんにちは！')
