from apps.product.models import Product
from apps.core.api.serializers.base_serializers import BaseSerializer
from apps.product.api.serializers.general_serializers import *


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


class ProductDetailSerializer(BaseSerializer):

    brand = BrandSerializer()
    category = CategorySerializer()
    measure_unit = MeasureUnitSerializer()

    class Meta:
        model = Product
        exclude = ['deleted']
