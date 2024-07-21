
from rest_framework import serializers

from apps.core.api.serializers.base_serializers import BaseSerializer
from apps.core.models import User


class UserSerializer(BaseSerializer):

    class Meta:
        model = User
        exclude = ['deleted', 'password', 'groups', 'user_permissions']
        custom_fields = ['username', 'email', 'name', 'last_name', 'is_active', 'image']
        methods = ['create', 'update', 'partial_update']


class SetPasswordSerializer(serializers.Serializer):
    password = serializers.CharField(write_only=True, required=True)
    confirm_password = serializers.CharField(write_only=True, required=True)

    def validate(self, data):
        if data['password'] != data['confirm_password']:
            raise serializers.ValidationError("As senhas não coincidem.")
        return data
