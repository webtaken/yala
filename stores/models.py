from django.db import models
from django.contrib.auth import get_user_model


class Store(models.Model):
    user = models.ForeignKey(
        get_user_model(),
        on_delete=models.CASCADE
    )
    name = models.CharField(max_length=150)
    description = models.TextField()
    dni = models.CharField(max_length=20)
    ruc = models.CharField(max_length=20)
    cci = models.CharField(max_length=50)
    whatsapp_number = models.CharField(max_length=50)

    def __str__(self):
        return f"{self.name}"
