from apps.core.api.serializers.address_serializers import AddressSerializer
from apps.core.api.serializers.base_serializers import BaseSerializer
from apps.core.models import Address, Supplier


class SupplierSerializer(BaseSerializer):
    address = AddressSerializer()

    class Meta:
        model = Supplier
        exclude = ['deleted']
        custom_fields = ['name', 'cellphone', 'active', 'address']
        methods = ['create', 'update', 'partial_update']

    def create(self, validated_data: dict):

        address_data: dict = validated_data.pop('address', None)
        address = Address(**address_data)
        address.save()

        supplier = Supplier(address=address, created_by=self.user, **validated_data)
        supplier.save()

        return supplier

    def update(self, instance: Supplier, validated_data: dict):
        address_data: dict = validated_data.pop('address', None)

        for attr, value in validated_data.items():
            setattr(instance, attr, value)
        
        if address_data:
            address: Address = instance.address
            for attr, value in address_data.items():
                setattr(address, attr, value)
            address.save()

        instance.save()
        return instance
