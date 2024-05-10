from djangochannelsrestframework.observer.generics import ObserverModelInstanceMixin, GenericAsyncAPIConsumer
from djangochannelsrestframework.observer import model_observer
from djangochannelsrestframework.mixins import ListModelMixin, RetrieveModelMixin
from djangochannelsrestframework import permissions
from djangochannelsrestframework.decorators import action


from comments.models import Comment
from comments.serializers import CommentSerializer


class CommentConsumer(GenericAsyncAPIConsumer, ListModelMixin):

    queryset = Comment.objects.filter(parent=None)
    serializer_class = CommentSerializer

    @model_observer(Comment)
    async def comment_activity(
        self,
        message: CommentSerializer,
        observer=None,
        subscribing_request_ids=[],
        **kwargs
    ):
        await self.send_json(dict(message.data))

    @comment_activity.serializer
    def comment_activity(self, instance: Comment, action, **kwargs) -> CommentSerializer:
        """This will return the comment serializer"""
        return CommentSerializer(instance)

    @action()
    async def subscribe_to_comment_activity(self, request_id, **kwargs):
        await self.comment_activity.subscribe(request_id=request_id)

