from rest_framework.viewsets import ModelViewSet


from accounts.models import CustomUser
from accounts.serializers import CustomUserSerializer

# TODO Permissions to be implemented


class CustomUserViewSet(ModelViewSet):
    """ CustomUser Viewset to handle base model operations. """

    queryset = CustomUser.objects.all().order_by("-date_created")
    serializer_class = CustomUserSerializer
