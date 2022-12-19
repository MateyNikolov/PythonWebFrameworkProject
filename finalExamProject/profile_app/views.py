from django.contrib import messages
from django.contrib.auth import get_user_model
from django.contrib.auth.mixins import LoginRequiredMixin
import django.contrib.auth.views as auth_views

from django.urls import reverse_lazy
from django.views import generic as views

from finalExamProject.profile_app.forms import EditProfileForm, ChangePasswordForm
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

    def get_success_url(self):
        user_pk = self.kwargs['pk']
        return reverse_lazy('show profile', kwargs={'pk': user_pk})


class DeleteProfileView(views.DeleteView, LoginRequiredMixin):
    template_name = 'profile/delete_profile.html'
    model = UserModel
    success_url = reverse_lazy('home')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        context['profile'] = Profile.objects.get(pk=self.request.user.pk)

        return context


class ChangePassword(auth_views.PasswordChangeView):
    template_name = 'profile/change_password.html'
    form_class = ChangePasswordForm

    def form_valid(self, form):
        form.save()
        messages.success(self.request, "Your password has been changed.")
        return super(ChangePassword, self).form_valid(form)

    def get_success_url(self):
        user_pk = self.request.user.pk
        return reverse_lazy('show profile', kwargs={'pk': user_pk})
