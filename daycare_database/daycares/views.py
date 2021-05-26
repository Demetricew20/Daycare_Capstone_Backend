from django.urls import reverse_lazy, reverse
from rest_framework import viewsets
from django.views import generic
from .serializers import DaycareSerializer
from .models import Daycare


class UserView(viewsets.ModelViewSet):
    queryset = Daycare.objects.all()
    serializer_class = DaycareSerializer
