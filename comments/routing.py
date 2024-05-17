from django.urls import path

from comments.consumers import CommentConsumer

websocket_urlpatterns = [
    path("ws/", CommentConsumer.as_asgi())
]
