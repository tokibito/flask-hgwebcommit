from flaskext.wtf import Form
from flaskext.wtf import SelectMultipleField, IntegerField, HiddenField, TextField, SelectField
from flaskext.wtf import HiddenInput, Required

class SelectFileForm(Form):
    files = SelectMultipleField('Files', validators=[Required()])

class SelectFileConfirmForm(SelectFileForm):
    confirm = IntegerField(widget=HiddenInput())

class SelectFileSubmitConfirmForm(SelectFileConfirmForm):
    operation = HiddenField(validators=[Required()])
    commit_message = TextField('Commit message')

class SelectActionForm(Form):
    action = SelectField('Action', validators=[Required()])
