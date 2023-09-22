from rest_framework import serializers

from apps.product.models import Product
from apps.core.api.serializers.base_serializers import BaseSerializer


class ProductSerializer(BaseSerializer):

    class Meta:
        model = Product
        exclude = ['deleted']
        custom_fields = ['description', 'brand', 'category', 'unit_quantity', 'measure_unit', 'active', 'image']
        methods = ['create', 'update', 'partial_update']

    def create(self, validated_data):
        validated_data['created_by'] = self.user
        return super().create(validated_data)
    
    def get_category(self, validated_data):
        return validated_data

    def to_representation(self, instance):
        representation = super().to_representation(instance)
        representation['brand'] = instance.brand.description
        representation['category'] = instance.category.description
        representation['measure_unit'] = instance.measure_unit.abbreviation
        return representation
