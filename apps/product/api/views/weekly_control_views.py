from rest_framework import viewsets

from apps.product.models import WeeklyControl
from apps.product.api.serializers.weekly_control_serializers import WeeklyControlSerializer


class WeeklyControlView(viewsets.ModelViewSet):
    queryset = WeeklyControl.objects.all()
    serializer_class = WeeklyControlSerializer
