from django.contrib.auth.models import Group
from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework.generics import RetrieveAPIView
from rest_framework.permissions import IsAuthenticated
from rest_framework_simplejwt import views as _views
from rest_framework import serializers
from .serializers import MyTokenObtainPairViewSerializer
from .models import NewUser


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = NewUser
        fields = ('id', 'user_name', 'password')


class MyTokenObtainPairView(_views.TokenObtainPairView):
    serializer_class = MyTokenObtainPairViewSerializer





