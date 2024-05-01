from apps.core.models import Supplier
from apps.product.models import Purchase, PriceProductSupplier, Price,WeeklyControlEvent
from apps.core.api.serializers.base_serializers import BaseSerializer


class PurchaseSerializer(BaseSerializer):

    class Meta:
        model = Purchase
        exclude = ['deleted']
        custom_fields = ['quantity', 'product', 'reference_day', 'supplier', 'weekly_control']
        methods = ['create', 'update', 'partial_update']

    def create(self, validated_data):
        weekly_control_event = WeeklyControlEvent(
            type=WeeklyControlEvent.Type.RECORD,
            new_value=validated_data['quantity'],
            reference_day=validated_data['reference_day'],
            supplier=validated_data['supplier'],
            weekly_control=validated_data['weekly_control'],
            created_by=self.user
        )
        weekly_control_event.save()

        return super().create(validated_data)
    

    def update(self, instance, validated_data):
        weekly_control_event = WeeklyControlEvent(
            type=WeeklyControlEvent.Type.RECORD,
            old_value=instance.quantity,
            new_value=validated_data['quantity'],
            reference_day=instance.reference_day,
            supplier=instance.supplier,
            weekly_control=instance.weekly_control,
            created_by=self.user
        )
        weekly_control_event.save()
        return super().update(instance, validated_data)
