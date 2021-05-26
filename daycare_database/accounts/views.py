from django.urls import reverse_lazy, reverse
from rest_framework import viewsets
from django.views import generic
from .forms import CustomUserForm
from .serializers import UserSerializer
from .models import User


class RegisterView(generic.CreateView):
    form_class = CustomUserForm


class UserView(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer

