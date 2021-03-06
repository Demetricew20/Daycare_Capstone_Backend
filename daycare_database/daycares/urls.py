from django.urls import path, include, re_path
from . import views
from rest_framework import routers

router = routers.DefaultRouter()
router.register('daycares', views.DaycareView),
router.register('age_groups', views.AgeGroupView),
router.register('child', views.ChildView),
router.register('parent', views.ParentView),
router.register('daycare_review', views.DaycareReviewView),

urlpatterns = [
    path('', include(router.urls)),
]