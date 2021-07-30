from django.contrib.auth.models import AbstractUser
from django.core.validators import RegexValidator
from django.db import models


class User(AbstractUser):
    """Модель пользователя системы."""

    country = models.CharField(max_length=50, blank=True)
    city = models.CharField(max_length=50, blank=True)
    zip = models.CharField(max_length=50, blank=True)
    phone = models.CharField(max_length=17, blank=True)
