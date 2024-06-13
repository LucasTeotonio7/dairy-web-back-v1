from rest_framework import serializers

from apps.product.models import Price, PriceProductSupplier, WeeklyControl, WeeklyControlEvent
from apps.core.api.serializers.base_serializers import BaseSerializer


class PriceSerializer(BaseSerializer):
    has_spreadsheet = serializers.SerializerMethodField()

    class Meta:
        model = Price
        exclude = ['deleted']
        custom_fields = ['value', 'description', 'default', 'product']
        methods = ['create', 'update', 'partial_update']

    def get_has_spreadsheet(self, obj):
        price: Price = obj
        if price.default:
            product = price.product
            weekly_control_exists = WeeklyControl.objects.filter(product=product).exists()
            return weekly_control_exists
        return False

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
            product = validated_data.get('product')
            Price.objects.filter(product=product, default=True).update(default=False)


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
            supplier=supplier, price__product=price.product,
        ).first()

        weekly_control_event = WeeklyControlEvent(
            type=WeeklyControlEvent.Type.PRICE,
            new_value=price.value,
            supplier=supplier,
            weekly_control_id=self.initial_data.get('weekly_control_id'),
            created_by=self.user
        )

        if price_product_supplier:
            
            if price_product_supplier.price == price:
                return price_product_supplier
            else:
                weekly_control_event.old_value = price_product_supplier.price.value
                weekly_control_event.save()

                price_product_supplier.price = price
                price_product_supplier.save()
                return price_product_supplier
        
        else:
            price_default = Price.objects.filter(
               default=True,
               product=price.product
            ).first()
            weekly_control_event.old_value = price_default.value
            weekly_control_event.save()

        return super().create(validated_data)
