from apps.product.models import MeasureUnit, Category, Brand
from apps.core.api.serializers.base_serializers import BaseSerializer


class MeasureUnitSerializer(BaseSerializer):

    class Meta:
        model = MeasureUnit
        exclude = ['deleted']
        custom_fields = ['description', 'abbreviation']
        methods = ['create', 'update', 'partial_update']


class CategorySerializer(BaseSerializer):

    class Meta:
        model = Category
        exclude = ['deleted']
        custom_fields = ['description']
        methods = ['create', 'update', 'partial_update']


class BrandSerializer(BaseSerializer):

    class Meta:
        model = Brand
        exclude = ['deleted']
        custom_fields = ['description']
        methods = ['create', 'update', 'partial_update']
