from django.db import models
from django.contrib.auth.models import User

class User(models.Model):
    email = models.EmailField(unique = True, null = False)
    phone = models.CharField(max_length = 12, null = False)
    fam = models.CharField(max_length = 64)
    name = models.CharField(max_length = 64)
    otc = models.CharField(max_length = 64)

class Coords(models.Model):
    latitude = models.FloatField()
    longitude = models.FloatField()
    height = models.IntegerField()

class Level(models.Model):
    winter = models.CharField(null = True, max_length = 2)
    spring = models.CharField(null = True, max_length = 2)
    summer = models.CharField(null = True, max_length = 2)
    autumn = models.CharField(null = True, max_length = 2)

class Mountain(models.Model):
    STATUS = [
        ('NEW', 'new'),
        ('PEN', 'pending'),
        ('ACC', 'accepted'),
        ('REJ', 'rejected')
    ]
    beauty_title = models.CharField(null = True, max_length = 64)
    title = models.CharField(null = True, max_length = 255)
    other_titles = models.CharField(null = True, max_length = 255)
    connect = models.CharField(null = True, max_length = 255)
    add_time = models.DateTimeField(auto_now_add = True)
    author = models.ForeignKey(User, on_delete = models.CASCADE)
    level = models.ForeignKey(Level, on_delete = models.CASCADE)
    coords = models.ForeignKey(Coords, on_delete = models.CASCADE)
    status = models.CharField(max_length = 3, choices = STATUS, default='NEW')

class ImagesOfMountains(models.Model):
    mountain = models.ForeignKey(Mountain, on_delete = models.CASCADE, related_name = 'images')
    data = models.URLField()
    title = models.CharField(null = True, max_length = 64)