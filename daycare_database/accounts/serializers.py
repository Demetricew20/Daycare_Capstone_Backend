from rest_framework import serializers, validators
from .models import User
from rest_framework_simplejwt import serializers as _serializers
from django.conf import settings


# class RegisterUserSerializer(serializers.ModelSerializer):
#
#     class Meta:
#         model = NewUser
#         fields = ('user_name','first_name', 'last_name', 'email', 'password', 'is_daycare')
#         extra_kwargs = {'password': {'write_only': True}}
#
#     def create(self, validated_data):
#         password = validated_data.pop('password', None)
#         instance = self.Meta.model(**validated_data)
#         if password is not None:
#             instance.set_password(password)
#         instance.save()
#         return instance

class UserSerializers(serializers.ModelSerializer):
    email = serializers.EmailField(
        required=True,
        validators=[validators.UniqueValidator(queryset=User.objects.all())]
    )
    username = serializers.CharField(
        max_length=32,
        validators=[validators.UniqueValidator(queryset=User.objects.all())]
    )
    password = serializers.CharField(max_length=32, write_only=True)
    is_daycare = serializers.BooleanField(default=False)
    first_name = serializers.CharField(max_length=75)
    last_name = serializers.CharField(max_length=75)

    def create(self, validate_data):
        user = User.objects.create_user(username=validate_data['username'], email=validate_data['email'],
                                           password=validate_data['password'], is_daycare=validate_data['is_daycare'],
                                           first_name=validate_data['first_name'], last_name=validate_data['last_name'])
        return user

    class Meta:
        model = User
        fields = ('id', 'username', 'email', 'password', 'is_daycare', 'first_name', 'last_name')


class UserViewSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'username', 'email', 'is_daycare', 'first_name', 'last_name')


class MyTokenObtainPairViewSerializer(_serializers.TokenObtainPairSerializer):

    @classmethod
    def get_token(cls, user):
        token = super().get_token(user)

        token['username'] = user.username
        token['email'] = user.email
        token['first_name'] = user.first_name
        token['last_name'] = user.last_name
        token['is_daycare'] = user.is_daycare

        return token
