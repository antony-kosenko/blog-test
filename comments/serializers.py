from django.core.exceptions import ObjectDoesNotExist
from django.db import transaction

from rest_framework import serializers

from accounts.serializers import BaseCustomUserSerializer
from accounts.models import CustomUser

from comments.models import Comment, Rate


class NewCommentSerializer(serializers.ModelSerializer):
    """ Serializes response for newly created comment """

    user = BaseCustomUserSerializer(read_only=True)

    class Meta:
        model = Comment
        exclude = ('level', 'lft', 'rght', 'tree_id')
        read_only_fields = ('date_created', )


class CommentRecusrsiveChildField(serializers.Serializer):
    """ Comment field for nested objects serialization. """
    def to_representation(self, instance):
        serializer = self.parent.parent.__class__(
            instance,
            context=self.context
        )
        serializer_data = serializer.data
        return serializer_data


class CommentSerializer(serializers.ModelSerializer):
    """ Serializes Comment model data. """

    user = BaseCustomUserSerializer()
    children = CommentRecusrsiveChildField(many=True, read_only=True)
    rate = serializers.SerializerMethodField(read_only=True)

    class Meta:
        model = Comment
        exclude = ('level', 'lft', 'rght', 'tree_id')
        read_only_fields = ('date_created', 'children')

    def get_rate(self, obj):
        """ Returns a rate sum. """
        return obj.get_rating()

    def create(self, validated_data):
        """
        Modified create method handle additional user creation
        while creating new Comment by anonymous user.
        """
        user_data = validated_data.pop('user')
        try:
            user = CustomUser.objects.get(pk=user_data.get('uuid'))
        except ObjectDoesNotExist:
            # performing atomic transaction to insure both instances created
            with transaction.atomic():
                new_user = CustomUser.objects.create(**user_data)
                comment = Comment.objects.create(
                    user=new_user,
                    **validated_data
                )
            return comment
        else:
            comment = Comment.objects.create(user=user, **validated_data)
            return comment


class RateSerializer(serializers.ModelSerializer):
    """ Serializes Rate create method """

    class Meta:
        model = Rate
        fields = '__all__'
