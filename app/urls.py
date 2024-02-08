from django.urls import path
from .views import (
    HomeView,
    LoginView,
    RegisterView,
    DashboardView,
    validate_login,
    user_login,
)

app_name = 'app'

htmx_urlpatterns = [
    path('login/validate-login/', validate_login, name='validate-login'),
    path('login/user-login/', user_login, name='user-login')
]

urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    path('login/', LoginView.as_view(), name='login'),
    # path('register/', RegisterView.as_view(), name='register'),
    path('dashboard/', DashboardView.as_view(), name='dashboard')
] + htmx_urlpatterns
