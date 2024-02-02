from django.http import HttpResponse, HttpRequest
from django.views import View
from django.core.validators import EmailValidator, MinLengthValidator
from django.core.exceptions import ValidationError
from django.shortcuts import render


class HomeView(View):
    def get(self, request, *args, **kwargs):
        return render(request, 'app/home.html', {})


class LoginView(View):
    def get(self, request, *args, **kwargs):
        return render(request, 'app/login.html', {})


class RegisterView(View):
    def get(self, request, *args, **kwargs):
        return render(request, 'app/register.html', {})


def validate_login(request: HttpRequest):
    email = request.POST.get('email', None)
    password = request.POST.get('password', None)
    email_validator = EmailValidator(message="Escribe un e-mail válido")
    password_validator = MinLengthValidator(
        limit_value=8, message="La contraseña debe ser mínimo de 8 caracteres"
    )

    if email:
        try:
            email_validator(email)
            return HttpResponse("")
        except ValidationError as e:
            return HttpResponse(e.message)
    if password:
        try:
            password_validator(password)
            return HttpResponse("")
        except ValidationError as e:
            return HttpResponse(e.message)

    return HttpResponse("")
