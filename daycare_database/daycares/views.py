from django.urls import reverse_lazy, reverse
from rest_framework import viewsets
from django.views import generic
from .serializers import DaycareSerializer, AgeGroupSerializer, ChildSerializer, ParentSerializer
from .models import Daycare, AgeGroup, Child, Parent, AgeGroupRoles


class DaycareView(viewsets.ModelViewSet):
    queryset = Daycare.objects.all()
    serializer_class = DaycareSerializer


class AgeGroupView(viewsets.ModelViewSet):
    queryset = AgeGroup.objects.all()
    serializer_class = AgeGroupSerializer


class ChildView(viewsets.ModelViewSet):
    queryset = Child.objects.all()
    serializer_class = ChildSerializer


class ParentView(viewsets.ModelViewSet):
    queryset = Parent.objects.all()
    serializer_class = ParentSerializer

