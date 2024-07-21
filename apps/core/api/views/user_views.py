from drf_spectacular.utils import extend_schema
from rest_framework import viewsets

from apps.core.api.serializers.user_serializers import UserSerializer
from apps.core.components import Paginator
from apps.core.models import User


@extend_schema(tags=['User', ])
class UserView(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    pagination_class = Paginator

    def get_queryset(self):
        queryset = super().get_queryset()
        queryset = queryset.filter(deleted=None)
        return queryset
