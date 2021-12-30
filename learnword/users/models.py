#file: users/models.py

from django.db import models

# Create your models here.

class User(models.Model):
    username = models.CharField("user_name", max_length=30, unique=True)
    password = models.CharField("password", max_length=32)
