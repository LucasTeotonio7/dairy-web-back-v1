from rest_framework import serializers

from apps.product.models import WeeklyControl
from apps.core.api.serializers.base_serializers import BaseSerializer


class WeeklyControlSerializer(BaseSerializer):
    product_description = serializers.CharField(source='product.description')

    class Meta:
        model = WeeklyControl
        fields = ['id','product_description', 'start_date', 'end_date', 'is_closed', 'product', 'created_by', 'created_at', 'updated_at']
        custom_fields = ['start_date', 'end_date', 'is_closed', 'product']
        methods = ['create', 'update', 'partial_update']

    def create(self, validated_data):
        validated_data['created_by'] = self.user
        return super().create(validated_data)
