from django import forms
from django.shortcuts import render
import django.views.generic as view
from django.urls import reverse_lazy

from finalExamProject.skins.models import Guns


class CreateRifleForm(forms.ModelForm):
    class Meta:
        model = Guns
        fields = '__all__'
        exclude = ('user',)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['description'].widget.attrs['style'] = 'resize: none;'


class ShowAllSkinsView(view.TemplateView):
    template_name = 'skins/show_all_skins.html'


class ShowAllRiflesView(view.ListView):
    template_name = 'skins/show_all_rifles.html'
    model = Guns


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
    pass


class AddContainerView(view.CreateView):
    pass
