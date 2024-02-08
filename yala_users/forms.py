from django import forms
from django.forms import ModelForm
from .models import YalaUser


class YalaUserRegisterForm(ModelForm):
    class Meta:
        model = YalaUser
        fields = (
            'email',
            'first_name',
            'last_name',
            'dni',
            'date_of_birth',
            'cellphone',
        )
