import django.views.generic as view
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy

from finalExamProject.skins.forms import CreateRifleForm, CreateAgentForm, CreateContainerForm, RifleEditForm, \
    AgentEditForm, ContainerEditForm
from finalExamProject.skins.models import Guns, Agent, Container


class ShowAllSkinsView(view.TemplateView):
    template_name = 'skins/show_all_skins.html'


class ShowAllRiflesView(view.ListView):
    template_name = 'skins/rifle/show_all_rifles.html'
    model = Guns
    paginate_by = 3


class ShowAllAgentsView(view.ListView):
    template_name = 'skins/agent/show_all_agents.html'
    model = Agent
    paginate_by = 3


class ShowAllContainersView(view.ListView):
    template_name = 'skins/container/show_all_containers.html'
    model = Container
    paginate_by = 3


class AddSkinView(view.TemplateView, LoginRequiredMixin):
    template_name = 'skins/add_skin.html'


class AddRifleView(view.CreateView, LoginRequiredMixin):
    template_name = 'skins/rifle/add_rifle.html'
    model = Guns
    form_class = CreateRifleForm
    success_url = reverse_lazy('all rifles')

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)


class AddAgentView(view.CreateView, LoginRequiredMixin):
    template_name = 'skins/agent/add_agent.html'
    model = Agent
    form_class = CreateAgentForm
    success_url = reverse_lazy('all agents')

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)


class AddContainerView(view.CreateView, LoginRequiredMixin):
    template_name = 'skins/container/add_container.html'
    model = Container
    form_class = CreateContainerForm
    success_url = reverse_lazy('all containers')

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)


class MySkinsView(view.ListView, LoginRequiredMixin):
    template_name = 'skins/show_only_my_skins.html'
    model = Guns
    paginate_by = 3

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['guns_objects'] = Guns.objects.filter(user_id=self.request.user.pk)
        context['agent_objects'] = Agent.objects.filter(user_id=self.request.user.pk)
        context['container_objects'] = Container.objects.filter(user_id=self.request.user.pk)
        return context


class ShowRifleDetailsView(view.DetailView, LoginRequiredMixin):
    template_name = 'skins/rifle/rifle_details.html'
    model = Guns

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['obj'] = self.object
        context['is_owner'] = self.object.user_id == self.request.user.pk
        return context


class ShowAgentDetailsView(view.DetailView, LoginRequiredMixin):
    template_name = 'skins/agent/agent_details.html'
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


class ShowContainerDetailsView(view.DetailView, LoginRequiredMixin):
    template_name = 'skins/container/container_details.html'
    model = Container

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['obj'] = self.object
        context['is_owner'] = self.object.user_id == self.request.user.pk
        type_to_split = context['obj'].type.split('_')
        context['obj'].type_to_show = ' '.join(type_to_split)
        return context


class RifleEditView(view.UpdateView, LoginRequiredMixin):
    template_name = 'skins/rifle/rifle_edit.html'
    model = Guns
    form_class = RifleEditForm

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['obj'] = self.object
        return context

    def get_success_url(self):
        rifle_pk = self.kwargs['pk']
        return reverse_lazy('rifle details', kwargs={'pk': rifle_pk})


class RifleDeleteView(view.DeleteView, LoginRequiredMixin):
    template_name = 'skins/rifle/rifle_delete.html'
    model = Guns
    success_url = reverse_lazy('my skins')


class AgentEditView(view.UpdateView, LoginRequiredMixin):
    template_name = 'skins/agent/agent_edit.html'
    model = Agent
    form_class = AgentEditForm

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['obj'] = self.object
        return context

    def get_success_url(self):
        agent_pk = self.kwargs['pk']
        return reverse_lazy('agent details', kwargs={'pk': agent_pk})


class AgentDeleteView(view.DeleteView, LoginRequiredMixin):
    template_name = 'skins/agent/agent_delete.html'
    model = Agent
    success_url = reverse_lazy('my skins')


class ContainerEditView(view.UpdateView, LoginRequiredMixin):
    template_name = 'skins/container/container_edit.html'
    model = Container
    form_class = ContainerEditForm

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['obj'] = self.object
        return context

    def get_success_url(self):
        container_pk = self.kwargs['pk']
        return reverse_lazy('container details', kwargs={'pk': container_pk})


class ContainerDeleteView(view.DeleteView, LoginRequiredMixin):
    template_name = 'skins/container/container_delete.html'
    model = Container
    success_url = reverse_lazy('my skins')
