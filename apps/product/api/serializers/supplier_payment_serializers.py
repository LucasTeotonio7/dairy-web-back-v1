from apps.product.models import SupplierPayment, WeeklyControlEvent
from apps.core.api.serializers.base_serializers import BaseSerializer


class SupplierPaymentSerializer(BaseSerializer):

    class Meta:
        model = SupplierPayment
        exclude = ['deleted']
        custom_fields = ['quantity', 'unit_price', 'supplier', 'weekly_control']
        methods = ['create', 'update', 'partial_update']

    def create(self, validated_data):
        total = validated_data['quantity'] * validated_data['unit_price']
        weekly_control_event = WeeklyControlEvent(
            type=WeeklyControlEvent.Type.PAYMENT,
            new_value=total,
            supplier=validated_data['supplier'],
            weekly_control=validated_data['weekly_control'],
            created_by=self.user
        )
        weekly_control_event.save()

        return super().create(validated_data)
