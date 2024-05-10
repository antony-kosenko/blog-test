from django.core.exceptions import ObjectDoesNotExist
from django.db import transaction

from rest_framework import serializers

from accounts.serializers import BaseCustomUserSerializer
from accounts.models import CustomUser

from comments.models import Comment, Rate


class CommentSerializer(serializers.ModelSerializer):
    """ Serializes Comment model data. """

    user = BaseCustomUserSerializer()
    rate = serializers.SerializerMethodField(read_only=True)

    class Meta:
        model = Comment
        exclude = ('level', 'lft', 'rght', 'tree_id')
        read_only_fields = ('date_created', )

    def get_rate(self, obj):
        """ Returns a rate sum. """
        return obj.get_rating()

    def get_fields(self):
        fields = super(CommentSerializer, self).get_fields()
        fields['children'] = CommentSerializer(many=True, required=False, read_only=True)
        return fields

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
                comment = Comment.objects.create(user=new_user, **validated_data)
            return comment
        else:
            comment = Comment.objects.create(user=user, **validated_data)
            return comment


class RateCreateSerializer(serializers.ModelSerializer):
    """ Serializes Rate create method """

    class Meta:
        model = Rate
        fields = '__all__'


class RateUpdateSerializer(serializers.ModelSerializer):
    """ Serializes Rate update method."""

    class Meta:
        model = Rate
        fields = '__all__'
