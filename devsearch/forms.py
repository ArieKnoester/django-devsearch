from django.contrib.auth.forms import SetPasswordForm


# Override the SetPasswordForm to add the css input styling to fields
class CustomSetPasswordForm(SetPasswordForm):
    def __init__(self, user, *args, **kwargs):
        self.user = user
        super(SetPasswordForm, self).__init__(*args, **kwargs)

        for name, field in self.fields.items():
            field.widget.attrs.update({'class': 'input'})