from rest_framework import serializers

from apps.product.models import MeasureUnit, Category, Brand
from apps.product.api.serializers.base_serializers import BaseSerializer

class MeasureUnitSerializer(BaseSerializer):

    class Meta:
        model = MeasureUnit
        exclude = ['deleted']
        custom_fields = ['description', 'abbreviation']
        methods = ['create', 'update', 'partial_update']

