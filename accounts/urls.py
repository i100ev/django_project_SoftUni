from django.urls import path
from accounts.views import AccountRegistrationView

urlpatterns = [
    path('accounts/register/', AccountRegistrationView.as_view(), name='register'),
]
