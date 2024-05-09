from django.urls import path

from comments.views import test_view

urlpatterns = [
    path("", test_view)
]