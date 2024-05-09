from rest_framework import serializers

from accounts.models import CustomUser


class CustomUserSerializer(serializers.ModelSerializer):
    """ CustomUser core serializer to process an instance's data.  """
    password = serializers.CharField(write_only=True, required=False)
    last_login = serializers.DateTimeField(read_only=True)
    is_superuser = serializers.BooleanField(read_only=True)
    is_staff = serializers.BooleanField(read_only=True)
    is_active = serializers.BooleanField(default=True)

    class Meta:
        model = CustomUser
        fields = '__all__'
        read_only_fields = ('groups', 'user_permissions')
