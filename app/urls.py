from django.urls import path
from .views import (
    HomeView,
    LoginView,
    RegisterView,
    validate_login,
)

app_name = 'app'

htmx_urlpatterns = [
    path('login/validate-login/', validate_login, name='validate-login')
]

urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    path('login/', LoginView.as_view(), name='login'),
    path('register/', RegisterView.as_view(), name='register'),
] + htmx_urlpatterns
