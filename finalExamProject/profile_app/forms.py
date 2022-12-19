from django import forms
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm, PasswordChangeForm

from finalExamProject.core.validators.validators import validate_age_is_above_16
from finalExamProject.profile_app.models import Profile


UserModel = get_user_model()


class EditProfileForm(forms.ModelForm):
    MAX_STEAMID_LENGTH = 15

    picture = forms.URLField()

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
        model = Profile
        fields = ("steam_ID", "age", "picture")


class ChangePasswordForm(PasswordChangeForm):
    old_password = forms.CharField(
        label="Old password",
        widget=forms.PasswordInput(
            attrs={"placeholder": "Enter old password"}
        ),
    )
    new_password1 = forms.CharField(
        label="New password",
        widget=forms.PasswordInput(attrs={"placeholder": "Enter new password"}),
        strip=False,
    )
    new_password2 = forms.CharField(
        label="New password confirmation",
        strip=False,
        widget=forms.PasswordInput(attrs={"placeholder": "Confirm new password"}),
    )



