from django.contrib.auth.forms import PasswordChangeForm
from django.contrib.auth.views import PasswordChangeView
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views import generic
from accounts.forms import AccountRegistrationForm, AccountEditForm


class AccountRegistrationView(generic.CreateView):
    form_class = AccountRegistrationForm
    template_name = 'registration/register.html'
    success_url = reverse_lazy('login')


class AccountEditView(generic.UpdateView):
    form_class = AccountEditForm
    template_name = 'registration/edit_profile.html'
    success_url = reverse_lazy('index')

    def get_object(self):
        return self.request.user


class PasswordsChangeView(PasswordChangeView):
    form_class = PasswordChangeForm
    template_name = 'registration/change_password.html'
    success_url = reverse_lazy('index')
