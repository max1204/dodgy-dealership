"""Module for custom"""
from django.contrib.auth.backends import ModelBackend
from django.contrib.auth import get_user_model


class CustomLogin(ModelBackend):
    """Custom backend for Email Login"""

    def authenticate(self, request, **kwargs):
        email = kwargs['username']
        password = kwargs['password']
        try:
            user = get_user_model().objects.get(email=email)
            if user.check_password(password) is True:
                return user
        except get_user_model().DoesNotExist:
            pass
        return None
