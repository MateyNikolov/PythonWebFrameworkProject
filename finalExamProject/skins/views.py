from django import forms
import django.views.generic as view
from django.urls import reverse_lazy

from finalExamProject.skins.models import Guns, Agent, Container


class CreateRifleForm(forms.ModelForm):
    class Meta:
        model = Guns
        fields = '__all__'
        exclude = ('user',)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['description'].widget.attrs['style'] = 'resize: none;'


class CreateAgentForm(forms.ModelForm):
    class Meta:
        model = Agent
        fields = '__all__'
        exclude = ('user',)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['description'].widget.attrs['style'] = 'resize: none;'


class CreateContainerForm(forms.ModelForm):
    class Meta:
        model = Container
        fields = "__all__"
        exclude = ('user',)


class ShowAllSkinsView(view.TemplateView):
    template_name = 'skins/show_all_skins.html'


class ShowAllRiflesView(view.ListView):
    template_name = 'skins/show_all_rifles.html'
    model = Guns


class ShowAllAgentsView(view.ListView):
    template_name = 'skins/show_all_agents.html'
    model = Agent


class ShowAllContainersView(view.ListView):
    template_name = 'skins/show_all_containers.html'
    model = Container


class AddSkinView(view.TemplateView):
    template_name = 'skins/add_skin.html'


class AddRifleView(view.CreateView):
    template_name = 'skins/add_rifle.html'
    model = Guns
    form_class = CreateRifleForm
    success_url = reverse_lazy('all rifles')

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)


class AddAgentView(view.CreateView):
    template_name = 'skins/add_agent.html'
    model = Agent
    form_class = CreateAgentForm
    success_url = reverse_lazy('all agents')

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)


class AddContainerView(view.CreateView):
    template_name = 'skins/add_container.html'
    model = Container
    form_class = CreateContainerForm
    success_url = reverse_lazy('all containers')

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)


class MySkinsView(view.ListView):
    template_name = 'skins/show_only_my_skins.html'
    model = Guns

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['guns_objects'] = Guns.objects.filter(user_id=self.request.user.pk)
        context['agent_objects'] = Agent.objects.filter(user_id=self.request.user.pk)
        context['container_objects'] = Container.objects.filter(user_id=self.request.user.pk)
        return context


class ShowGunDetailsView(view.DetailView):
    template_name = 'skins/gun_details.html'
    model = Guns

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['obj'] = self.object
        context['is_owner'] = self.object.user_id == self.request.user.pk
        return context


class ShowAgentDetailsView(view.DetailView):
    template_name = 'skins/agent_details.html'
    model = Agent

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['obj'] = self.object
        context['is_owner'] = self.object.user_id == self.request.user.pk
        if context['obj'].side == 't_side':
            context['obj'].side_to_show = 'T Side'
        else:
            context['obj'].side_to_show = 'CT Side'
        return context


class ShowContainerDetailsView(view.DetailView):
    template_name = 'skins/container_details.html'
    model = Container

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['obj'] = self.object
        context['is_owner'] = self.object.user_id == self.request.user.pk
        type_to_split = context['obj'].type.split('_')
        context['obj'].type_to_show = ' '.join(type_to_split)

        return context
