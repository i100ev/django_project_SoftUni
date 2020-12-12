from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
from datetime import datetime, date
from ckeditor.fields import RichTextField


class Post(models.Model):
    title = models.CharField(max_length=255)
    post_image = models.ImageField(upload_to='posts', null=True, blank=True)
    subtitle = models.CharField(max_length=255)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    body = RichTextField(blank=True, null=True)
    date_published = models.DateTimeField(auto_now_add=True)
    likes = models.ManyToManyField(User, related_name='post_likes')

    def likes_count(self):
        return self.likes.count()

    def __str__(self):
        return self.title + ' | ' + self.author.username

    def get_absolute_url(self):
        """
        return a string that refer to the object over HTTP
        """
        return reverse('full post', args=[str(self.id)])
