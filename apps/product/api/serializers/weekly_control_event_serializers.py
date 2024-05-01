from apps.product.models import WeeklyControlEvent
from apps.core.api.serializers.base_serializers import BaseSerializer


class WeeklyControlEventSerializer(BaseSerializer):

    class Meta:
        model = WeeklyControlEvent
        exclude = ['deleted']
        custom_fields = ['start_date', 'end_date', 'is_closed', 'product']
        methods = ['create']

    def create(self, validated_data):
        validated_data['created_by'] = self.user
        return super().create(validated_data)
