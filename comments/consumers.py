from djangochannelsrestframework.observer.generics import GenericAsyncAPIConsumer
from djangochannelsrestframework.mixins import ListModelMixin
from djangochannelsrestframework.observer import model_observer
from djangochannelsrestframework.decorators import action
from rest_framework.permissions import AllowAny

from comments.models import Comment
from comments.serializers import CommentSerializer, NewCommentSerializer


class CommentConsumer(ListModelMixin, GenericAsyncAPIConsumer):
    queryset = (
        Comment.objects.filter(level=0)
        .select_related("user", "parent")
        .prefetch_related("children")
        .order_by("-date_created")
        )
    serializer_class = CommentSerializer
    permission_classes = (AllowAny, )

    @action()
    async def subscribe_to_comment_activity(self, request_id, **kwargs):
        await self.comment_activity.subscribe(request_id=request_id)

    @model_observer(Comment)
    async def comment_activity(
        self,
        message: NewCommentSerializer,
        observer=None,
        subscribing_request_ids=[],
        **kwargs
    ):
        await self.send_json(dict(message.data))

    @comment_activity.serializer
    def comment_activity(self, instance: Comment, action, **kwargs) -> NewCommentSerializer:
        """Returns the comment serializer"""
        return NewCommentSerializer(instance)
