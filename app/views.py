from django.http import HttpRequest, HttpResponse
from django.views import View
from django.shortcuts import render
from django.contrib.auth import get_user_model
from django.contrib.auth.mixins import LoginRequiredMixin
from allauth.account.admin import EmailAddress


class HomeView(View):
    def get(self, request, *args, **kwargs):
        return render(request, 'app/home.html', {})


class DashboardView(LoginRequiredMixin, View):
    def get(self, request, *args, **kwargs):
        email_verified = EmailAddress.objects.filter(
            user=self.request.user, verified=True
        ).exists()
        context = {
            "email_verified": email_verified
        }
        return render(request, 'app/dashboard.html', context)


def check_email_exists(request: HttpRequest, *args, **kwargs):
    email = request.GET.get("email")
    email_already_picked = get_user_model().objects.filter(email=email).exists()
    print(email_already_picked)
    if email_already_picked:
        return HttpResponse("Este correo ya está registrado")
    return HttpResponse("")
