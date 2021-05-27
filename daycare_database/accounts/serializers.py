from rest_framework import serializers
from .models import NewUser
from rest_framework_simplejwt import serializers as _serializers
from django.conf import settings


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = NewUser
        fields = ('id', 'first_name', 'last_name', 'user_name', 'email', 'password', 'is_daycare')


class MyTokenObtainPairViewSerializer(_serializers.TokenObtainPairSerializer):

    def validate(self, attrs):
        data = super().validate(attrs)
        refresh = self.get_token(self.user)
        data['refresh'] = str(refresh)
        data.pop('refresh', None) # remove refresh from the payload
        data['access'] = str(refresh.access_token)

        # Add extra responses here
        data['user_name'] = self.user.user_name
        data['is_daycare'] = self.user.is_daycare
        data['first_name'] = self.user.first_name
        data['last_name'] = self.user.last_name
        return data

