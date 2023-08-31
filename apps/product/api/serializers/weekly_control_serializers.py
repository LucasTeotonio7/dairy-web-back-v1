from apps.product.models import WeeklyControl
from apps.core.api.serializers.base_serializers import BaseSerializer


class WeeklyControlSerializer(BaseSerializer):

    class Meta:
        model = WeeklyControl
        exclude = ['deleted']
        custom_fields = ['start_date', 'end_date', 'is_closed', 'product']
        methods = ['create', 'update', 'partial_update']

    def create(self, validated_data):
        validated_data['created_by'] = self.user
        return super().create(validated_data)