from django.conf import settings
from django.contrib.auth.models import AnonymousUser
from rest_framework import authentication
from rest_framework import exceptions

class ApiUser():
    @property
    def is_authenticated(self):
        return True

class ApiAuthentication(authentication.BaseAuthentication):
    def authenticate(self, request):
        auth = authentication.get_authorization_header(request) or b''
        auth = auth.decode('utf-8').split(' ')

        if not auth or auth[0].lower() != 'token':
            return None

        if len(auth) == 1:
            msg = _('Invalid token header. No credentials provided.')
            raise exceptions.AuthenticationFailed(msg)
        elif len(auth) > 2:
            msg = _('Invalid token header. Credentials string should not contain spaces.')
            raise exceptions.AuthenticationFailed(msg)

        token = auth[1]

        if token == settings.API_TOKEN:
            return (ApiUser(), token)
        else:
            raise exceptions.AuthenticationFailed('Unauthorized')
