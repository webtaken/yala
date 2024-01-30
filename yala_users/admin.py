from django.contrib import admin

from .models import YalaUser


# Now register the new UserAdmin...
admin.site.register(YalaUser)
