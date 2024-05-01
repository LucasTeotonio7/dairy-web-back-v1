from drf_spectacular.utils import extend_schema
from rest_framework import viewsets

from apps.core.components.paginator import Paginator
from apps.product.models import WeeklyControlEvent
from apps.product.api.serializers.weekly_control_event_serializers import WeeklyControlEventSerializer


@extend_schema(tags=['Weekly Control Event', ])
class WeeklyControlEventView(viewsets.ModelViewSet):
    queryset = WeeklyControlEvent.objects.all()
    serializer_class = WeeklyControlEventSerializer
    pagination_class = Paginator
    http_method_names = ['get', 'post']

    def get_queryset(self):
        queryset = super().get_queryset()
        supplier_id = self.request.query_params.get('supplier_id')
        weekly_control_id = self.request.query_params.get('weekly_control_id')

        if supplier_id:
            queryset = queryset.filter(supplier=supplier_id)
        if weekly_control_id:
            queryset = queryset.filter(weekly_control=weekly_control_id)
        return queryset
