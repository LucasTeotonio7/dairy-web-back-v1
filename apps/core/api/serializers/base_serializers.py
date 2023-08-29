from rest_framework import serializers


class BaseSerializer(serializers.ModelSerializer):

    class Meta:
        methods = None
        custom_fields = None

    def get_fields(self):
        fields = super().get_fields()

        if not hasattr(self.Meta, 'methods') or not hasattr(self.Meta, 'custom_fields'):
            return fields

        if self.context['view'].action in self.Meta.methods:
            fields = {field: fields[field] for field in self.Meta.custom_fields if field in fields}

        return fields
