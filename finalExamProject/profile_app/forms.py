from django import forms

from finalExamProject.core.validators.validators import validate_age_is_above_16
from finalExamProject.profile_app.models import Profile


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