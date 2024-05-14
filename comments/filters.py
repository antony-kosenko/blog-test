import django_filters as filters
from django_filters import rest_framework

from comments.models import Comment


class CommentFilter(rest_framework.FilterSet):
    username = filters.CharFilter(
        field_name='user__username',
        lookup_expr='iexact',
        label="Username"
        )
    email = filters.CharFilter(
        field_name='user__email',
        lookup_expr='iexact',
        label="Email"
        )
    date_created = filters.IsoDateTimeFromToRangeFilter(
        lookup_expr='icontains',
        )
    ordering = filters.OrderingFilter(
        fields=(
        ('user__username', 'username'),
        ('user__email', 'email'),
        ('date_created', 'date_created')
        )
    )

    class Meta:
        model = Comment
        fields = ('parent', 'date_created', 'username')