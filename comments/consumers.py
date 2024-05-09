from djangochannelsrestframework.generics import GenericAsyncAPIConsumer
from djangochannelsrestframework.observer.generics import ObserverModelInstanceMixin
from djangochannelsrestframework.mixins import ListModelMixin, RetrieveModelMixin
from djangochannelsrestframework import permissions


from comments.models import Comment
from comments.serializers import CommentSerializer


class CommentConsumer(
        ObserverModelInstanceMixin,
        ListModelMixin,
        RetrieveModelMixin,
        GenericAsyncAPIConsumer
):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
    permission_classes = (permissions.AllowAny,)

