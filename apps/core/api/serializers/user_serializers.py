from apps.core.api.serializers.base_serializers import BaseSerializer
from apps.core.models import User


class UserSerializer(BaseSerializer):

    class Meta:
        model = User
        exclude = ['deleted', 'password']
        custom_fields = ['username', 'email', 'name', 'last_name', 'is_active', 'image']
        methods = ['create', 'update', 'partial_update']
