from drf_spectacular.utils import extend_schema
from rest_framework import viewsets

from apps.core.models import Supplier
from apps.core.api.serializers.supplier_serializers import SupplierSerializer


@extend_schema(tags=['Supplier', ])
class SupplierView(viewsets.ModelViewSet):
    queryset = Supplier.objects.all()
    serializer_class = SupplierSerializer
