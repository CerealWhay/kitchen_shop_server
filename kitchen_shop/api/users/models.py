from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    """Модель пользователя системы."""


class Customer(models.Model):
    first_name = models.CharField(max_length=200)
    last_name = models.CharField(max_length=200)
    email = models.CharField(max_length=200)
    phone = models.CharField(max_length=17)

    country = models.CharField(max_length=50)
    city = models.CharField(max_length=50)
    zip = models.CharField(max_length=50)

    sessionid = models.CharField(max_length=200, default='', blank=False, unique=True)

    def __str__(self):
        return self.email


class Appeal(models.Model):
    name = models.CharField(max_length=200)
    email = models.CharField(max_length=200)
    phone = models.CharField(max_length=17)
    message = models.TextField(max_length=500)

    sessionid = models.CharField(max_length=200, default='', blank=False, unique=True)

    def __str__(self):
        return self.email