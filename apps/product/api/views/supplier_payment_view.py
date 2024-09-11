from drf_spectacular.utils import extend_schema
from rest_framework import viewsets, status
from rest_framework.decorators import action
from rest_framework.response import Response

from apps.product.models import SupplierPayment
from apps.product.api.serializers.supplier_payment_serializers import SupplierPaymentSerializer
from apps.product.services import get_analysis_big_numbers, get_analysis_by_month, get_analysis_by_supplier


@extend_schema(tags=['Supplier payment', ])
class SupplierPaymentView(viewsets.ModelViewSet):
    queryset = SupplierPayment.objects.all()
    serializer_class = SupplierPaymentSerializer

    @action(detail=False, methods=['get'], url_path='analysis')
    def get_analysis(self, request):
        data = get_analysis_big_numbers()
        data['month_to_month'] = get_analysis_by_month()
        data['main_suppliers'] = get_analysis_by_supplier()
        return Response(data=data, status=status.HTTP_200_OK)
