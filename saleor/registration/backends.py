from django.contrib.auth import get_user_model
from django.contrib.auth.backends import ModelBackend

from .models import ExternalUserData

User = get_user_model()


class Backend(ModelBackend):

    def get_user(self, user_id):
        try:
            return User.objects.get(pk=user_id)
        except User.DoesNotExist:
            return None


class UsernamePasswordBackend(Backend):
    """Authentication backend that expects an mobile in username parameter."""

    def authenticate(self, username=None, password=None, **_kwargs):
        try:
            user = User.objects.get(mobile=username)
        except User.DoesNotExist:
            return None
        if user.check_password(password):
            return user

class MobilePasswordBackend(Backend):
    """Authentication backend that expects mobile and password parameters."""

    def authenticate(self, mobile=None, password=None, **_kwargs):
        try:
            user = User.objects.get(mobile=mobile)
        except User.DoesNotExist:
            return None
        if user.check_password(password):
            return user


class ExternalLoginBackend(Backend):
    """Authenticate with external service id."""

    def authenticate(self, service=None, username=None, **_kwargs):
        try:
            user_data = (ExternalUserData.objects
                                         .select_related('user')
                                         .get(service=service,
                                              username=username))
            return user_data.user
        except ExternalUserData.DoesNotExist:
            return None


class TrivialBackend(Backend):
    """Authenticate with user instance."""

    def authenticate(self, user=None, **_kwargs):
        if isinstance(user, User):
            return user
