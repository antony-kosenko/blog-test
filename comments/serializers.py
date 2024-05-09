from rest_framework import serializers

from accounts.serializers import BaseCustomUserSerializer

from comments.models import Comment, Rate


class CommentSerializer(serializers.ModelSerializer):
    """ Serializes Comment model data. """

    class Meta:
        model = Comment
        exclude = ("user", )
        read_only_fields = ('date_created', )


class RateSerializer(serializers.ModelSerializer):
    """ Serializes Rate model data. """

    class Meta:
        model = Rate
        fields = '__all__'
