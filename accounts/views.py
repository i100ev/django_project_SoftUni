from django.shortcuts import render
from django.views import generic
from django.contrib.auth.forms import UserCreationForm


class AccountRegistrationView(generic.CreateView):
    form_class = UserCreationForm
    template_name = 'registration/register.html'
    success_url = 'registration/login.html'
