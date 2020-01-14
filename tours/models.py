from django.db import models
from django.contrib.auth.models import User
from django.contrib.auth import get_user_model
from django.utils.datetime_safe import datetime


class Tour(models.Model):
    title = models.CharField(max_length=255)
    presentation = models.TextField()
    detail = models.TextField()
    date_and_price = models.TextField()
    map = models.ImageField(upload_to='images/map')
    category = models.ForeignKey('Category', on_delete=models.CASCADE, related_name='tour')

    def __str__(self):
        return f'{self.title}'


class Images(models.Model):
    tour = models.ForeignKey(Tour, on_delete=models.CASCADE, related_name='images')
    images = models.ImageField(upload_to='images/portfolio')


class Category(models.Model):
    category = models.CharField(max_length=50)

    def __str__(self):
        return self.category


class Comment(models.Model):
    tour = models.ForeignKey(Tour, on_delete=models.CASCADE, related_name='comments', )
    body = models.CharField(max_length=255)
    author = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)
    date = models.DateField(default=datetime.now)

    def __str__(self):
        return f'{self.body}, {self.author}'

