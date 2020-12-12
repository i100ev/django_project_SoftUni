from django import forms

from blog.models import Post
from core.BootstrapFormMixin import BootstrapFormMixin


class PostCreateForm(forms.ModelForm, BootstrapFormMixin):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.setup_form()

    class Meta:
        model = Post
        fields = ('title', 'subtitle', 'post_image', 'author', 'body')

        widgets = {
            'author': forms.TextInput(attrs={'value': '', 'id': 'author-id', 'type': 'hidden'}),
        }


class PostEditForm(forms.ModelForm, BootstrapFormMixin):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.setup_form()

    class Meta:
        model = Post
        fields = ('title', 'subtitle', 'post_image', 'body')


