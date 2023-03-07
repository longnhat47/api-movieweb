from unicodedata import category
from django.db import models
from accounts.models import User

# Create your models here.


class Category(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Country(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Movie(models.Model):
    category = models.ForeignKey(
        Category, related_name='categories', null=True, on_delete=models.SET_NULL)
    country = models.ForeignKey(
        Country, related_name='country', null=True, on_delete=models.SET_NULL)
    thumbnail = models.ImageField(upload_to='thumbnails')
    name = models.CharField(max_length=255, blank=False)
    description = models.TextField()
    video = models.FileField(upload_to='movies')
    created_at = models.DateTimeField(auto_now_add=True)
    status = models.BooleanField(default=True)

    def __str__(self):
        return self.name


class Comment(models.Model):
    movie = models.ForeignKey(
        Movie, related_name='comments', on_delete=models.CASCADE)
    user = models.ForeignKey(User, related_name='user_comment',
                             on_delete=models.CASCADE)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.movie
