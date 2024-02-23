from django.db import models
from django.utils import timezone
from django.contrib.auth import get_user_model


class Profile(models.Model):
    user = models.OneToOneField(
        get_user_model(),
        on_delete=models.PROTECT,
        primary_key=True,
    )
    dni = models.CharField(max_length=20)
    date_of_birth = models.DateField(blank=True, null=True)
    date_joined = models.DateTimeField(default=timezone.now)
    last_login = models.DateTimeField(blank=True, null=True)
    cellphone = models.CharField(max_length=20)

    def __str__(self):
        return f"{self.user}"
