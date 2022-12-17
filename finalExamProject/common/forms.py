import django.forms as forms

from finalExamProject.common.models import Comment


class CreateCommentForm(forms.ModelForm):

    class Meta:
        model = Comment
        fields = '__all__'
        exclude = ('user', 'picture',)
        widgets = {
            'comment_text': forms.Textarea(
                attrs={
                    'cols': 70,
                    'rows': 2,
                    'placeholder': 'Add comment...',
                    'label': '',
                },
            ),

        }
        label = ''

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['comment_text'].widget.attrs['style'] = 'resize: none;'
        self.fields['comment_text'].label = ""
