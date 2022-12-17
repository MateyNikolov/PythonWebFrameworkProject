from django.contrib.auth import get_user_model
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.views import generic as views

from finalExamProject.profile_app.forms import EditProfileForm
from finalExamProject.profile_app.models import Profile
from finalExamProject.skins.models import Guns, Agent, Container

UserModel = get_user_model()


class ShowProfileView(views.DetailView, LoginRequiredMixin):
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


class EditProfileView(views.UpdateView, LoginRequiredMixin):
    template_name = 'profile/edit_profile.html'
    model = Profile
    form_class = EditProfileForm
    success_url = reverse_lazy('home')


class DeleteProfileView(views.DeleteView, LoginRequiredMixin):
    template_name = 'profile/delete_profile.html'
    model = UserModel
    success_url = reverse_lazy('login')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        context['profile'] = Profile.objects.get(pk=self.request.user.pk)

        return context
