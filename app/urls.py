from django.urls import path
from .views import (
    HomeView,
    DashboardView,
    check_email_exists,
)

app_name = 'app'

htmx_urlpatterns = [
    path("check-email-exists/", check_email_exists, name="check-email-exists")
]

urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    path('dashboard/', DashboardView.as_view(), name='dashboard')
] + htmx_urlpatterns
