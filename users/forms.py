from django.forms import ModelForm
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import Profile, Skill


class CustomUserCreationForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['first_name', 'email', 'username', 'password1', 'password2']
        labels = {
            'first_name': 'Name'
        }

    def __init__(self, *args, **kwargs):
        super(CustomUserCreationForm, self).__init__(*args, **kwargs)

        for name, field in self.fields.items():
            field.widget.attrs.update({'class': 'input'})


class ProfileForm(ModelForm):
    class Meta:
        model = Profile
        fields = [
            'name',
            'username',
            'location',
            'email',
            'short_intro',
            'bio',
            'profile_image',
            'social_github',
            'social_twitter',
            'social_linkedin',
            'social_youtube',
            'social_website'
        ]
        # This would be the easier way to exclude the 'user' field from the form.
        # However, it's recommended to explicitly list fields to include instead.
        # This method can lead to security vulnerabilities, especially if new fields
        # are added and 'exclude' is not updated.
        # exclude = ('user',)

    def __init__(self, *args, **kwargs):
        super(ProfileForm, self).__init__(*args, **kwargs)

        for name, field in self.fields.items():
            field.widget.attrs.update({'class': 'input'})


class SkillForm(ModelForm):
    class Meta:
        model = Skill
        fields = ['name', 'description']


    def __init__(self, *args, **kwargs):
        super(SkillForm, self).__init__(*args, **kwargs)

        for name, field in self.fields.items():
            field.widget.attrs.update({'class': 'input'})