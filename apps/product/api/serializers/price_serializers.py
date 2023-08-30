from rest_framework.exceptions import ValidationError

from apps.product.models import Price, PriceProductSupplier
from apps.core.api.serializers.base_serializers import BaseSerializer


class PriceSerializer(BaseSerializer):

    class Meta:
        model = Price
        exclude = ['deleted']
        custom_fields = ['value', 'description', 'default', 'product']
        methods = ['create', 'update', 'partial_update']

    def create(self, validated_data: dict):
        validated_data['created_by'] = self.user
        self.set_default_price(validated_data)
        return super().create(validated_data)

    def update(self, instance, validated_data):
        self.set_default_price(validated_data)
        return super().update(instance, validated_data)
    
    def set_default_price(self, validated_data: dict):

        default = validated_data.get('default', False)
        if default:
            Price.objects.filter(default=True).update(default=False)


class PriceProductSupplierSerializer(BaseSerializer):

    class Meta:
        model = PriceProductSupplier
        exclude = ['deleted']
        custom_fields = ['price', 'supplier']
        methods = ['create', 'update', 'partial_update']

    def create(self, validated_data: dict):
        price = validated_data.get('price')
        supplier = validated_data.get('supplier')

        price_product_supplier = PriceProductSupplier.objects.filter(
            supplier=supplier
        ).first()

        if price_product_supplier:
            
            if price_product_supplier.price == price:
                return price_product_supplier
            else:
                price_product_supplier.price = price
                price_product_supplier.save()
                return price_product_supplier

        return super().create(validated_data)
