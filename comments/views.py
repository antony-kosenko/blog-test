from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet
from rest_framework.generics import CreateAPIView, UpdateAPIView

from comments.models import Comment, Rate
from comments.serializers import (
    CommentSerializer,
    RateCreateSerializer,
    RateUpdateSerializer
)


def test_view(request):
    # TODO to be removed
    return render(request, template_name="comments/test.html")


class CommentViewSet(ModelViewSet):
    """ Comment Viewset to handle base model operations. """

    queryset = Comment.objects.filter(level=0)
    serializer_class = CommentSerializer


class RatingCreateView(CreateAPIView):
    """ Rating viewset for Comment rating featuring """
    queryset = Rate.objects.all()
    serializer_class = RateCreateSerializer


class RatingUpdateView(UpdateAPIView):
    """ Performs Rate instance update. """
    queryset = Rate.objects.all()
    serializer_class = RateUpdateSerializer
