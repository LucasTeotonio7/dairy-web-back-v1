from apps.product.models import SupplierPayment
from apps.core.api.serializers.base_serializers import BaseSerializer


class SupplierPaymentSerializer(BaseSerializer):

    class Meta:
        model = SupplierPayment
        exclude = ['deleted']
        custom_fields = ['quantity', 'unit_price', 'supplier', 'weekly_control']
        methods = ['create', 'update', 'partial_update']
