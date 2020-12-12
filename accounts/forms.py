from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django.contrib.auth.models import User
from django import forms

from accounts.models import UserProfile
from core.BootstrapFormMixin import BootstrapFormMixin


class AccountRegistrationForm(UserCreationForm, BootstrapFormMixin):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.setup_form()

    email = forms.EmailField(widget=forms.EmailInput())
    first_name = forms.CharField(max_length='25')
    last_name = forms.CharField(max_length='25')

    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'email', 'password1', 'password2')


class AccountEditForm(UserChangeForm, BootstrapFormMixin):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.setup_form()

    email = forms.EmailField(widget=forms.EmailInput())
    first_name = forms.CharField(max_length='25')
    last_name = forms.CharField(max_length='25')

    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'email')


class UserProfileInfoForm(forms.ModelForm, BootstrapFormMixin):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.setup_form()

    class Meta:
        model = UserProfile
        fields = ('profile_picture', 'short_bio',)


