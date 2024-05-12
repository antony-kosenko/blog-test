from django.db import IntegrityError
from django.shortcuts import render

from rest_framework import status
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet, GenericViewSet
from rest_framework.decorators import action
from rest_framework.mixins import CreateModelMixin, UpdateModelMixin
from rest_framework.exceptions import ValidationError, ParseError

from comments.models import Comment, Rate
from comments.services import RateService
from comments.serializers import CommentSerializer, NewCommentSerializer, RateSerializer
from comments.utils import captcha_valid


def test_view(request):
    # TODO to be removed
    return render(request, template_name="comments/test.html")


class CommentViewSet(ModelViewSet):
    """ Comment Viewset to handle base model operations. """

    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
    authentication_classes = []
    permission_classes = (AllowAny,)

    def create(self, request, *args, **kwargs):
        try:
            captcha_validated = captcha_valid(request_data=request.data)
        except ValidationError as e:
            return Response(e.detail, status=e.status_code)
        except ParseError as e:
            return Response(e.detail, status=e.status_code)
        else:
            if not captcha_validated:
                return Response({"captcha": "validation failed."}, status=status.HTTP_403_FORBIDDEN)
            return super().create(request, *args, **kwargs)

    @action(detail=True, methods=["post", "get"], url_path="rate/(?P<rate_type>[^/.]+)")
    def rate_set(self, request, rate_type: str, pk=None):
        """ Increases comment rating. """
        comment = self.get_object()
        user = self.request.user
        try:
            rate = RateService.set_rate(instance=comment, user=user, action=rate_type)
        except ValueError as e:
            return Response({"rate": str(e)}, status=status.HTTP_406_NOT_ACCEPTABLE)
        except IntegrityError as e:
            return Response({"rate": str(e)}, status=status.HTTP_400_BAD_REQUEST)

        else:
            serializer = RateSerializer(rate)
            return Response({"rate": serializer.data}, status=status.HTTP_201_CREATED)


class RatingViewSet(
    CreateModelMixin,
    UpdateModelMixin,
    GenericViewSet
):
    """ Rating base viewset. """

    queryset = Rate.objects.all()
    serializer_class = RateSerializer
