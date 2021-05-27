from django.urls import reverse_lazy, reverse
from rest_framework import viewsets
from .serializers import DaycareSerializer, AgeGroupSerializer, ChildSerializer, ParentSerializer, \
    DaycareReviewSerializer
from .models import Daycare, AgeGroup, Child, Parent, DaycareReview


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


class DaycareReviewView(viewsets.ModelViewSet):
    queryset = DaycareReview.objects.all()
    serializer_class = DaycareReviewSerializer

