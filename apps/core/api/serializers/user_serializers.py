
from rest_framework import serializers
from django.contrib.auth.models import Group

from apps.core.api.serializers.base_serializers import BaseSerializer
from apps.core.models import User


class GroupSerializer(serializers.ModelSerializer):
    class Meta:
        model = Group
        fields = ['id', 'name'] 


class UserSerializer(BaseSerializer):
    available_groups = serializers.SerializerMethodField()
    groups = serializers.PrimaryKeyRelatedField(
        queryset=Group.objects.all(),
        many=True,
        required=False
    )

    class Meta:
        model = User
        exclude = ['deleted', 'password', 'user_permissions']
        custom_fields = ['username', 'email', 'name', 'last_name', 'is_active', 'image', 'groups']
        methods = ['create', 'update', 'partial_update']

    def get_available_groups(self, obj):
        return Group.objects.values('id', 'name')


class SetPasswordSerializer(serializers.Serializer):
    password = serializers.CharField(write_only=True, required=True)
    confirm_password = serializers.CharField(write_only=True, required=True)

    def validate(self, data):
        if data['password'] != data['confirm_password']:
            raise serializers.ValidationError("As senhas não coincidem.")
        return data
