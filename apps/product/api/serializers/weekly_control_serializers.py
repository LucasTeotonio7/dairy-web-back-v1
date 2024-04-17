from rest_framework import serializers

from apps.product.models import WeeklyControl, Purchase
from apps.product.services import get_weekly_control_purchases_by_supplier
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

class WeeklyControlDetailSerializer(serializers.ModelSerializer):
    product_description = serializers.CharField(source='product.description')

    class Meta:
        model = WeeklyControl
        fields = '__all__'

    def to_representation(self, instance):
        data = super().to_representation(instance)
        supplier_id = None
        context: dict = self._kwargs.get('context')
        request = context.get('request')
        params: dict = request.query_params
        supplier_id = params.get('supplier_id')
        data['suppliers'] = get_weekly_control_purchases_by_supplier(instance, supplier_id)
        data['purchase_exists'] = Purchase.objects.filter(weekly_control=instance).exists()
        return data
