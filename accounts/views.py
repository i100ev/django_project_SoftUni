from django.contrib.auth.forms import PasswordChangeForm
from django.contrib.auth.views import PasswordChangeView
from django.urls import reverse_lazy
from django.views.generic import CreateView, UpdateView

from accounts.forms import AccountRegistrationForm, AccountEditForm, UserProfileInfoForm
from accounts.models import UserProfile


class AccountRegistrationView(CreateView):
    form_class = AccountRegistrationForm
    template_name = 'registration/register.html'
    success_url = reverse_lazy('login')


class AccountEditView(UpdateView):
    form_class = AccountEditForm
    template_name = 'registration/edit_profile.html'
    success_url = reverse_lazy('index')

    def get_object(self):
        return self.request.user


class PasswordsChangeView(PasswordChangeView):
    form_class = PasswordChangeForm
    template_name = 'registration/change_password.html'
    success_url = reverse_lazy('index')


class CreateProfileInfoView(CreateView):
    model = UserProfile
    template_name = 'profile/create_profile_info.html'
    success_url = reverse_lazy('index')
    fields = ('profile_picture', 'short_bio',)

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)


class EditProfileInfoView(UpdateView):
    model = UserProfile
    form_class = UserProfileInfoForm
    template_name = 'profile/edit_profile_info.html'
    success_url = reverse_lazy('index')
