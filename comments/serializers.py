from rest_framework import serializers
from rest_framework.utils.serializer_helpers import ReturnDict
from accounts.serializers import BaseCustomUserSerializer

from comments.models import Comment, Rate


class CommentSerializer(serializers.ModelSerializer):
    """ Serializes Comment model data. """
    user = serializers.UUIDField()

    class Meta:
        model = Comment
        exclude = ('level', 'lft', 'rght', 'tree_id')
        read_only_fields = ('date_created', )

    def get_fields(self):
        fields = super(CommentSerializer, self).get_fields()
        fields['children'] = CommentSerializer(many=True, required=False)
        return fields


class RateSerializer(serializers.ModelSerializer):
    """ Serializes Rate model data. """

    class Meta:
        model = Rate
        fields = '__all__'
