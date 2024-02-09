from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import YalaUser


admin.site.register(YalaUser, UserAdmin)
