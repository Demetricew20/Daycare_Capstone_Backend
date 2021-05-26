from django.urls import path, include
from . import views
from rest_framework import routers

router = routers.DefaultRouter()
router.register('daycares', views.DaycareView),
router.register('age_groups', views.AgeGroupView),

urlpatterns = [
    path('', include(router.urls)),
    path('', include(router.urls))
]