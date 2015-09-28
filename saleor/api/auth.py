__author__ = 'hkalra'

from django.conf import settings
from django.db.models.signals import post_save
from django.dispatch import receiver
from rest_framework.authtoken.models import Token

#from rest_framework import authentication
#from rest_framework import exceptions
#from saleor.userprofile.models import User





'''
class ExampleAuthentication(authentication.BaseAuthentication):
    def authenticate(self, request):
        #print(request.META)
        mobile = request.META.get('username')
        #print(mobile)
        if not mobile:
            return None

        try:
            user = User.objects.get(mobile=mobile)
        except User.DoesNotExist:
            raise exceptions.AuthenticationFailed('No such user')

        return (user, None)





class AlwaysRootBackend(object):

    def authenticate(self, username=None, password=None, **_kwargs):
        try:

            #print(mobile)
            print(_kwargs)
            user = User.objects.get(mobile=username)

        except User.DoesNotExist:
            print('User not found')
            for user in User.objects.all():
                print(user)
            return None
        if user.check_password(password):
            return user


    def authenticate(self, *args, **kwargs):
        """Always returns the `root` user.  DO NOT USE THIS IN PRODUCTION!"""
        return User.objects.get(mobile='9980470200')

    def get_user(self, user_id):
        return User.objects.get(mobile=user_id)
'''

