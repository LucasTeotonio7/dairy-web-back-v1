from rest_framework import serializers

from apps.core.models import User
from apps.product.models import WeeklyControlEvent
from apps.core.api.serializers.base_serializers import BaseSerializer


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'username', 'email', 'name', 'last_name', 'image', 'is_active', 'is_staff')


class WeeklyControlEventSerializer(BaseSerializer):

    created_by = UserSerializer()
    measure_unit = serializers.CharField(source='weekly_control.product.measure_unit.abbreviation')

    class Meta:
        model = WeeklyControlEvent
        exclude = ['deleted']
        custom_fields = ['type', 'description', 'old_value', 'new_value', 'reference_day', 'supplier', 'weekly_control']
        methods = ['create']

    def create(self, validated_data):
        validated_data['created_by'] = self.user
        return super().create(validated_data)
