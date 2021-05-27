from rest_framework import serializers
from .models import NewUser


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = NewUser
        fields = ('id', 'first_name', 'last_name', 'username', 'email', 'password', 'is_daycare')
