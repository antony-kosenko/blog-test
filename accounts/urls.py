from django.urls import path, include
from rest_framework.routers import DefaultRouter

from accounts.views import CustomUserViewSet


app_name = "accounts"

# routers:
router = DefaultRouter()
router.register('', CustomUserViewSet, basename='user')

urlpatterns = [
    path('', include(router.urls))
]
