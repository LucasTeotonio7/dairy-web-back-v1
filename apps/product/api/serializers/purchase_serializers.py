from apps.product.models import Purchase
from apps.core.api.serializers.base_serializers import BaseSerializer


class PurchaseSerializer(BaseSerializer):

    class Meta:
        model = Purchase
        exclude = ['deleted']
        custom_fields = ['quantity', 'is_closed', 'product', 'reference_day', 'supplier']
        methods = ['create', 'update', 'partial_update']

    def create(self, validated_data):
        validated_data['created_by'] = self.user
        return super().create(validated_data)
