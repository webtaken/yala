from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils import timezone


class Profile(models.Model):
    email = models.EmailField(
        verbose_name="email address",
        max_length=255,
        unique=True,
    )
    dni = models.CharField(max_length=20)
    date_of_birth = models.DateField(blank=True, null=True)
    date_joined = models.DateTimeField(default=timezone.now)
    last_login = models.DateTimeField(blank=True, null=True)
    cellphone = models.CharField(max_length=20)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username']
