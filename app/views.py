from django.http import HttpResponse, HttpRequest
from django_htmx.http import HttpResponseClientRedirect
from django.views import View
from django.shortcuts import render, redirect
from django.urls import reverse
from django.contrib.auth import authenticate, login
from django.contrib.auth.mixins import LoginRequiredMixin
from .utils import login_form_validation
from allauth.account.forms import LoginForm, SignupForm
# from yala_users.forms import YalaUserRegisterForm
from allauth.account.admin import EmailAddress


class HomeView(View):
    def get(self, request, *args, **kwargs):
        return render(request, 'app/home.html', {})


class LoginView(View):
    def get(self, request, *args, **kwargs):
        context = {
            "email_validation": "",
            "password_validation": "",
        }
        return render(request, 'app/login.html', context)


class RegisterView(View):
    def get(self, request: HttpRequest, *args, **kwargs):
        return render(request, 'app/register.html', {})


class DashboardView(LoginRequiredMixin, View):
    def get(self, request, *args, **kwargs):
        email_verified = EmailAddress.objects.filter(
            user=self.request.user, verified=True
        ).exists()
        context = {
            "email_verified": email_verified
        }
        return render(request, 'app/dashboard.html', context)


def validate_login(request: HttpRequest):
    email = request.POST.get('email', None)
    password = request.POST.get('password', None)
    field = request.GET.get('field', None)
    errors = login_form_validation(email, password)
    if field == 'email':
        return HttpResponse("<br>".join(errors["email_errors"]))
    if field == 'password':
        return HttpResponse("<br>".join(errors["password_errors"]))
    return HttpResponse("")


def validate_register(request: HttpRequest):
    email = request.POST.get('email', None)
    first_name = request.POST.get('first_name', None)
    last_name = request.POST.get('last_name', None)
    dni = request.POST.get('dni', None)
    birth_of_date = request.POST.get('birth_of_date', None)
    cellphone = request.POST.get('cellphone', None)
    password1 = request.GET.get('password1', None)
    password2 = request.GET.get('password2', None)
    return HttpResponse("")


def user_login(request: HttpRequest):
    email = request.POST.get('email', None)
    password = request.POST.get('password', None)
    errors = login_form_validation(email, password)
    context = {"email_validation": "", "password_validation": ""}
    has_errors = False
    for k, v in errors.items():
        has_errors = has_errors or len(v) > 0
        if k == 'email_errors':
            context["email_validation"] = v
        if k == 'password_errors':
            context["password_validation"] = v

    if not has_errors:
        user = authenticate(request, username=email, password=password)
        if user is not None:
            login(request, user)
            return HttpResponseClientRedirect(reverse('app:dashboard'))
        context["form_errors"] = ["El e-mail o la contraseña son incorrectos"]
    return render(request, 'app/partials/login_form.html', context)
