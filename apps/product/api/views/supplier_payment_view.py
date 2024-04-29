from drf_spectacular.utils import extend_schema
from rest_framework import viewsets

from apps.product.models import SupplierPayment
from apps.product.api.serializers.supplier_payment_serializers import SupplierPaymentSerializer


@extend_schema(tags=['Supplier payment', ])
class SupplierPaymentView(viewsets.ModelViewSet):
    queryset = SupplierPayment.objects.all()
    serializer_class = SupplierPaymentSerializer
