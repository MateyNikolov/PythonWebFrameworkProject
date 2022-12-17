import django.views.generic as view
from django.contrib.auth import get_user_model
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.views.generic import CreateView

from finalExamProject.common.forms import CreateCommentForm
from finalExamProject.common.models import Comment
from finalExamProject.profile_app.models import Profile

UserModel = get_user_model()


class ShowHomePageView(view.TemplateView):
    template_name = 'core/home.html'


class ShareExperienceView(LoginRequiredMixin, CreateView):
    model = Comment
    template_name = 'core/share-experience.html'
    form_class = CreateCommentForm
    success_url = reverse_lazy('share experience')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['user'] = UserModel
        context['comments'] = Comment.objects.all().order_by('-date')
        return context

    def form_valid(self, form):
        user_id = self.request.user.id
        profile = Profile.objects.get(user_id=self.request.user.id)
        self.object = form.save(commit=False)
        self.object.user_id = user_id
        self.object.picture = profile.picture
        self.object.save()
        return super().form_valid(form)
