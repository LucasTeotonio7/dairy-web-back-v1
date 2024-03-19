from apps.core.models import Supplier
from apps.product.models import Purchase, PriceProductSupplier, Price
from apps.core.api.serializers.base_serializers import BaseSerializer


class PurchaseSerializer(BaseSerializer):

    class Meta:
        model = Purchase
        exclude = ['deleted']
        custom_fields = ['quantity', 'is_closed', 'product', 'reference_day', 'supplier', 'weekly_control']
        methods = ['create', 'update', 'partial_update']

    def create(self, validated_data):
        validated_data['created_by'] = self.user
        supplier: Supplier = validated_data['supplier']
        price_table: PriceProductSupplier = supplier.priceproductsupplier_set.first()
        unit_price = 0.00
        if price_table:
            unit_price = price_table.price.value
        else:
            price_default = Price.objects.filter(
                product=validated_data['product'], 
                default=True
            ).first()
            if price_default:
                unit_price = price_default.value
        validated_data['unit_price'] = unit_price

        return super().create(validated_data)
