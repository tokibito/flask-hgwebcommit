# coding:utf8
from flaskext.wtf import Form
from flaskext.wtf import SelectMultipleField, IntegerField, HiddenField, TextField, SelectField
from flaskext.wtf import HiddenInput, Required

class SelectFileForm(Form):
    files = SelectMultipleField(u'Files', validators=[Required()])

class SelectFileConfirmForm(SelectFileForm):
    confirm = IntegerField(widget=HiddenInput())

class SelectFileSubmitConfirmForm(SelectFileConfirmForm):
    operation = HiddenField(validators=[Required()])
    commit_message = TextField(u'コミットメッセージ')

class SelectActionForm(Form):
    action = SelectField(u'Action', validators=[Required()])
