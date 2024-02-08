from django.contrib.auth.hashers import check_password
from django.contrib.auth.backends import BaseBackend
from .models import YalaUser


class YalaBackend(BaseBackend):
    # Create an authentication method
    # This is called by the standard Django login procedure
    def authenticate(self, email=None, password=None):
        try:
            # Try to find a user matching the email
            user = YalaUser.objects.get(email=email)

            #  Check the password is the reverse of the username
            if check_password(password, user.password):
                # Yes? return the Django user object
                return user
            else:
                # No? return None - triggers default login failed
                return None
        except YalaUser.DoesNotExist:
            # No user was found, return None - triggers default login failed
            return None

    # Required for your backend to work properly - unchanged in most scenarios
    def get_user(self, user_id):
        try:
            return YalaUser.objects.get(pk=user_id)
        except YalaUser.DoesNotExist:
            return None
