from flaskext.wtf import Form
from flaskext.wtf import SelectMultipleField, IntegerField, HiddenField, TextField, SelectField
from flaskext.wtf import HiddenInput, Required
from flaskext.babel import lazy_gettext as _

class SelectFileForm(Form):
    files = SelectMultipleField('Files', validators=[Required()])

class SelectFileConfirmForm(SelectFileForm):
    confirm = IntegerField(widget=HiddenInput())

class SelectFileSubmitConfirmForm(SelectFileConfirmForm):
    operation = HiddenField(validators=[Required()])
    commit_message = TextField(_('Commit message'))

class SelectActionForm(Form):
    action = SelectField('Action', validators=[Required()])
