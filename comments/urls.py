from django.urls import path, include

from rest_framework.routers import DefaultRouter

from comments.views import test_view, CommentViewSet, RatingViewSet

app_name = 'comments'

# routers:
router = DefaultRouter()
router.register('comments', CommentViewSet, basename='comment'),
router.register('ratings', RatingViewSet, basename='rating')

urlpatterns = [
    path('test/', test_view),
    path('', include(router.urls)),

]
