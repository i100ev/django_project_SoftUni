from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
from datetime import datetime, date


class Post(models.Model):
    title = models.CharField(max_length=255)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    body = models.TextField()
    date_published = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title + ' | ' + self.author.username

    def get_absolute_url(self):
        """
        Redirects user to newly created post
        """
        return reverse('full post', args=(str(self.id)))
