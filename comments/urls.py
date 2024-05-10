from django.urls import path, include

from rest_framework.routers import DefaultRouter

from comments.views import test_view, CommentViewSet, RatingCreateView, RatingUpdateView

app_name = 'comments'

# routers:
router = DefaultRouter()
router.register('comment/', CommentViewSet, basename='comment')

urlpatterns = [
    path('test/', test_view),
    path('', include(router.urls)),
    path('rates/', RatingCreateView.as_view(), name='add_rate'),
    path('rates/<int:pk>/', RatingUpdateView.as_view(), name='update_rate')
]
