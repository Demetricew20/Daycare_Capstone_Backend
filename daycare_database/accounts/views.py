from django.contrib.auth.models import Group
from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework.generics import RetrieveAPIView
from rest_framework.permissions import IsAuthenticated
from rest_framework_simplejwt import views as _views
from rest_framework import permissions, status
from django.contrib.auth.models import Group
from rest_framework.views import APIView
from .models import User
from .serializers import MyTokenObtainPairViewSerializer, UserSerializers, UserViewSerializer


class CustomUserRegister(APIView):
    permission_classes = [permissions.AllowAny]

    def post(self, request):
        reg_serializer = UserSerializers(data=request.data)
        if reg_serializer.is_valid():
            new_user = reg_serializer.save()
            if new_user:
                json = reg_serializer.data
                return Response(json, status=status.HTTP_201_CREATED)
        return Response(reg_serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class MyTokenObtainPairView(_views.TokenObtainPairView):
    serializer_class = MyTokenObtainPairViewSerializer


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserViewSerializer





