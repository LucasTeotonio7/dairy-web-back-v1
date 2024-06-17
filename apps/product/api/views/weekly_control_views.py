from drf_spectacular.utils import extend_schema
from rest_framework import viewsets, status
from rest_framework.response import Response

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

    def check_if_closed(self, weekly_control):
        if weekly_control.is_closed:
            return Response(
                data={'message': 'Closed spreadsheet cannot be changed.'},
                status=status.HTTP_403_FORBIDDEN
            )
        return None

    def update(self, request, *args, **kwargs):
        weekly_control: WeeklyControl = self.get_object()
        response = self.check_if_closed(weekly_control)
        if response:
            return response
        return super().update(request, *args, **kwargs)
    
    def destroy(self, request, *args, **kwargs):
        weekly_control: WeeklyControl = self.get_object()
        response = self.check_if_closed(weekly_control)
        if response:
            return response
        return super().destroy(request, *args, **kwargs)
