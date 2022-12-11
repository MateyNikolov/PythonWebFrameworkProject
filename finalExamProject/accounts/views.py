from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.views import generic as views
from django.contrib.auth import views as auth_views, get_user_model, login
from django.shortcuts import redirect

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


class SignInView(auth_views.LoginView):
    template_name = 'auth/login.html'
    success_url = reverse_lazy('home')
    redirect_authenticated_user = True

    def get_success_url(self):
        if self.success_url:
            return self.success_url

        return self.get_redirect_url() or self.get_default_redirect_url()


class SignUpView(views.CreateView):
    template_name = 'auth/register.html'
    form_class = UserForm
    model = UserModel
    success_url = reverse_lazy('home')

    def form_valid(self, form):
        result = super().form_valid(form)
        login(self.request, self.object)
        return result

    def get(self, request, *args, **kwargs):
        response = super().get(request, *args, **kwargs)
        if request.user.is_authenticated:
            return redirect('home')
        return response


class SignOutView(auth_views.LogoutView, LoginRequiredMixin):
    pass
