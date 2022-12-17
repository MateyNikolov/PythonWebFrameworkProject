from django import forms
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm

from finalExamProject.core.validators.validators import validate_age_is_above_16
from finalExamProject.profile_app.models import Profile

UserModel = get_user_model()


class UserForm(UserCreationForm):
    MAX_STEAMID_LENGTH = 15

    password1 = forms.CharField(
        label='Enter password',
        widget=forms.PasswordInput
    )
    password2 = forms.CharField(
        label='Confirm password',
        widget=forms.PasswordInput
    )
    steam_ID = forms.CharField(
        max_length=MAX_STEAMID_LENGTH,
        label='Enter Steam ID',
        required=True,
    )
    age = forms.IntegerField(
        label='Enter your age',
        validators=[validate_age_is_above_16],
    )

    class Meta:
        model = UserModel
        fields = ("username", "email", "password1", "password2", "steam_ID", "age")
        help_texts = {
            "username": None,
            "email": None,
        }

    def save(self, commit=True):
        user = super().save(commit=commit)
        steamID = self.cleaned_data['steam_ID']
        age = self.cleaned_data['age']
        profile = Profile(
            steam_ID=steamID,
            age=age,
            user=user,
        )
        if commit:
            profile.save()

        return user
