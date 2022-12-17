from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.views import generic as views
from django.contrib.auth import views as auth_views, get_user_model, login
from django.shortcuts import redirect

from finalExamProject.accounts.forms import UserForm

UserModel = get_user_model()


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
