
# from rest_framework_jwt.views import obtain_jwt_token
# from django.utils.translation import ugettext as _

from rest_framework_jwt.views import JSONWebTokenAPIView

from rest_framework import serializers
from rest_framework_jwt.compat import Serializer, PasswordField, get_username_field
# from allauth.account.models import EmailAddress, EmailConfirmation, EmailConfirmationHMAC

from django.contrib.auth import authenticate

from rest_framework_jwt.settings import api_settings



jwt_payload_handler = api_settings.JWT_PAYLOAD_HANDLER
jwt_encode_handler = api_settings.JWT_ENCODE_HANDLER

class JSONWebTokenSerializer(Serializer):
    """
    Serializer class used to validate a username and password.

    'username' is identified by the custom UserModel.USERNAME_FIELD.

    Returns a JSON Web Token that can be used to authenticate later calls.
    """

    def __init__(self, *args, **kwargs):
        """
        Dynamically add the USERNAME_FIELD to self.fields.
        """
        super(JSONWebTokenSerializer, self).__init__(*args, **kwargs)

        self.fields[self.username_field] = serializers.CharField()
        self.fields['password'] = PasswordField(write_only=True)

    @property
    def username_field(self):
        return get_username_field()

    def validate(self, attrs):
        credentials = {
            self.username_field: attrs.get(self.username_field),
            'password': attrs.get('password')
        }

        user = authenticate(**credentials)

        if user:
            remember_me = self.initial_data.get('rememberMe', True)
            payload = jwt_payload_handler( user)
            payload.update({'extra':'dummy data'})
            return {
                'token': jwt_encode_handler(payload),
                # 'user':user
            }
        else:
            raise serializers.ValidationError('UNABLE_TO_LOGIN_WITH_PROVIDED_CREDENTIALS')



class ObtainJSONWebToken(JSONWebTokenAPIView):
    """
    API View that receives a POST with a user's username and password.

    Returns a JSON Web Token that can be used for authenticated requests.
    """
    serializer_class = JSONWebTokenSerializer


obtain_jwt_token = ObtainJSONWebToken.as_view()