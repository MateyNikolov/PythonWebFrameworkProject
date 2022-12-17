from django import forms

from finalExamProject.skins.models import Guns, Agent, Container


class CreateRifleForm(forms.ModelForm):
    picture = forms.ImageField(
        required=True,
    )

    class Meta:
        model = Guns
        fields = '__all__'
        exclude = ('user',)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['description'].widget.attrs['style'] = 'resize: none;'


class CreateAgentForm(forms.ModelForm):
    picture = forms.ImageField(
        required=True,
    )

    class Meta:
        model = Agent
        fields = '__all__'
        exclude = ('user',)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['description'].widget.attrs['style'] = 'resize: none;'


class CreateContainerForm(forms.ModelForm):
    picture = forms.ImageField(
        required=True,
    )

    class Meta:
        model = Container
        fields = "__all__"
        exclude = ('user',)


class RifleEditForm(forms.ModelForm):
    picture = forms.ImageField(widget=forms.FileInput)

    class Meta:
        model = Guns
        fields = '__all__'
        exclude = ('user',)


class AgentEditForm(forms.ModelForm):
    picture = forms.ImageField(widget=forms.FileInput)

    class Meta:
        model = Agent
        fields = '__all__'
        exclude = ('user',)


class ContainerEditForm(forms.ModelForm):
    picture = forms.ImageField(widget=forms.FileInput)

    class Meta:
        model = Container
        fields = '__all__'
        exclude = ('user',)
