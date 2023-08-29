from rest_framework import serializers

from apps.core.models import Address


class AddressSerializer(serializers.ModelSerializer):

    class Meta:
        model = Address
        fields = ['street', 'number', 'zone', 'city', 'state', 'postal_code', 'complement']
