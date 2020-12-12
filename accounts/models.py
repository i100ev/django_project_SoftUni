from django.db import models
from django.contrib.auth.models import User


class UserProfile(models.Model):
    profile_picture = models.ImageField(upload_to='user_avatars', blank=True, null=True)
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    short_bio = models.TextField()

    def __str__(self):
        return self.user.username
