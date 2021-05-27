from django.urls import path, include
from . import views
from rest_framework import routers
from rest_framework_simplejwt import views as jwt_views
# router = routers.DefaultRouter()
# router.register('users', views.UserAPIView)

app_name = "accounts"
urlpatterns = [
    #path('api/user', views.UserAPIView.as_view(), name='user'),
    path('api/token/', views.MyTokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh', jwt_views.TokenRefreshView.as_view(), name='token_refresh')

]