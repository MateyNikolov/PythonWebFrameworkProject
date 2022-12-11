from django.contrib.auth import get_user_model
from django.views import generic as views

from finalExamProject.accounts.views import UserForm
from finalExamProject.profile_app.models import Profile

UserModel = get_user_model()


class ShowProfileView(views.DetailView):
    template_name = 'profile/show_profile.html'
    model = Profile

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['profile'] = self.object
        return context


class EditProfileView(views.UpdateView):
    template_name = 'profile/edit_profile.html'
    model = Profile
    form_class = UserForm


class DeleteProfileView(views.DeleteView):
    pass
