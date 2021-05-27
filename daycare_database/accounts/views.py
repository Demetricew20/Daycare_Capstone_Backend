from django.contrib.auth.models import Group
from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from rest_framework.views import APIView
from .serializers import UserSerializer
from .models import NewUser


class RegistrationView(APIView):
    pass


class UserView(viewsets.ModelViewSet):
    queryset = NewUser.objects.all()
    serializer_class = UserSerializer
    permission_classes = [IsAuthenticated]

