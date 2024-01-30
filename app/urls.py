from django.urls import include, re_path
from .views import HomeView

app_name = 'app'

urlpatterns = [
    re_path(r'', HomeView.as_view(), name='home')
]
