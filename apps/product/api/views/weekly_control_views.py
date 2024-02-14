from drf_spectacular.utils import extend_schema
from rest_framework import viewsets

from apps.core.components.paginator import Paginator
from apps.product.models import WeeklyControl
from apps.product.api.serializers.weekly_control_serializers import WeeklyControlSerializer, WeeklyControlDetailSerializer


@extend_schema(tags=['Weekly Control', ])
class WeeklyControlView(viewsets.ModelViewSet):
    queryset = WeeklyControl.objects.all()
    serializer_class = WeeklyControlSerializer
    pagination_class = Paginator

    def get_queryset(self):
        queryset = WeeklyControl.objects.all()
        return queryset.order_by('-created_at')
    

    def get_serializer_class(self):
        if self.action in ['retrieve']:
            return WeeklyControlDetailSerializer
        return super().get_serializer_class()
