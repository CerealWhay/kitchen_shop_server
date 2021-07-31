from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    """Модель пользователя системы."""


class Customer(models.Model):
    name = models.CharField(max_length=200, null=True, blank=True)
    email = models.CharField(max_length=200, null=True, blank=True)
    sessionid = models.CharField(max_length=200, null=False, blank=False, unique=True)

    def __str__(self):
        return self.sessionid
