from flaskext.wtf import Form
from flaskext.wtf import SelectMultipleField, IntegerField, HiddenField, TextField, SelectField
from flaskext.wtf import TextInput, HiddenInput, Required
from flaskext.babel import lazy_gettext as _


class SizedTextInput(TextInput):
    def __init__(self, size, input_type=None):
        super(SizedTextInput, self).__init__(input_type)
        self.size = size

    def __call__(self, field, **kwargs):
        if 'size' not in kwargs:
            kwargs['size'] = self.size
        return super(SizedTextInput, self).__call__(field, **kwargs)


class SelectFileForm(Form):
    files = SelectMultipleField('Files', validators=[Required()])


class SelectFileConfirmForm(SelectFileForm):
    confirm = IntegerField(widget=HiddenInput())


class SelectFileSubmitConfirmForm(SelectFileConfirmForm):
    operation = HiddenField(validators=[Required()])
    commit_message = TextField(_('Commit message'), widget=SizedTextInput(60))


class SelectActionForm(Form):
    action = SelectField('Action', validators=[Required()])


class ConfirmForm(Form):
    confirm = IntegerField(widget=HiddenInput(), validators=[Required()])
