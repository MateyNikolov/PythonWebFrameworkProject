from django import forms
from django.contrib.auth import get_user_model
from django.shortcuts import get_object_or_404
from django.urls import reverse_lazy
from django.views import generic as views

from finalExamProject.core.validators.validators import validate_age_is_above_16
from finalExamProject.profile_app.models import Profile
from finalExamProject.skins.models import Guns, Agent, Container

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


class ShowProfileView(views.DetailView):
    template_name = 'profile/show_profile.html'
    model = Profile

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['profile'] = self.object
        total_guns = len(list(Guns.objects.filter(user_id=self.object.pk)))
        total_agents = len(list(Agent.objects.filter(user_id=self.object.pk)))
        total_container = len(list(Container.objects.filter(user_id=self.object.pk)))
        context['profile'].total_skins = total_guns + total_agents + total_container
        return context


class EditProfileView(views.UpdateView):
    template_name = 'profile/edit_profile.html'
    model = Profile
    form_class = EditProfileForm
    success_url = reverse_lazy('home')


class DeleteProfileView(views.DeleteView):
    template_name = 'profile/delete_profile.html'
    model = UserModel
    success_url = reverse_lazy('login')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        context['profile'] = Profile.objects.get(pk=self.request.user.pk)

        return context
