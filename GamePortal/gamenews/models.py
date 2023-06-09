from django.db import models
from django.contrib.auth.models import User
from django.db.models import Sum

class Category(models.Model):
    name = models.CharField(max_length=20, unique=True)
    subscribers = models.ManyToManyField(User, related_name='categories')

    def __str__(self):
        return self.name


class Callboard(models.Model):
    headline = models.CharField(max_length=128)
    text = models.TextField()
    datetime_created = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)

    def get_absolute_url(self):
        return reverse('adv_detail', args=[self.pk])

    def __str__(self):
        return self.headline

class Reply(models.Model):
    text = models.CharField(max_length=170)
    datetime_created = models.DateTimeField(auto_now_add=True)
    approved = models.BooleanField(default=False)
    callb = models.ForeignKey(Callboard, on_delete=models.CASCADE, related_name='replies')
    user = models.ForeignKey(User, on_delete=models.CASCADE)
