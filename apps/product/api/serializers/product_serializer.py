from apps.product.models import Product
from apps.core.api.serializers.base_serializers import BaseSerializer


class ProductSerializer(BaseSerializer):

    class Meta:
        model = Product
        exclude = ['deleted']
        custom_fields = ['description', 'brand', 'category', 'measure_unit', 'active', 'image']
        methods = ['create', 'update', 'partial_update']

    def create(self, validated_data):
        validated_data['created_by'] = self.user
        return super().create(validated_data)
