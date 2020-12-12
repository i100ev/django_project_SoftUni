from django.urls import path
from django.contrib.auth import views as auth_views
from accounts.views import AccountRegistrationView, AccountEditView, PasswordsChangeView

urlpatterns = [
    path('accounts/register/', AccountRegistrationView.as_view(), name='register'),
    path('accounts/edit_profile/', AccountEditView.as_view(), name='edit profile'),
    path('accounts/password/', PasswordsChangeView.as_view(), name='change_password'),
]
