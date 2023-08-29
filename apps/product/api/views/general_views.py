from rest_framework import viewsets

from apps.product.models import MeasureUnit
from apps.product.api.serializers.general_serializers import MeasureUnitSerializer


class MeasureUnitView(viewsets.ModelViewSet):
    queryset = MeasureUnit.objects.all()
    serializer_class = MeasureUnitSerializer
    http_method_names = ['get', 'post', 'put', 'patch', 'delete']
