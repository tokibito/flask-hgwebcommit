from flask import flash

from hgwebcommit.actions.decorators import action

@action('hello', 'Hello')
def hello():
    flash('Hello!')
