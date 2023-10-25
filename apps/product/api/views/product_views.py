from drf_spectacular.utils import extend_schema
from rest_framework import viewsets

from apps.product.models import Product
from apps.product.api.serializers.product_serializers import ProductSerializer, ProductDetailSerializer


@extend_schema(tags=['Product', ])
class ProductView(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

    def get_serializer_class(self):
        if self.action in ['list', 'retrieve']:
            return ProductDetailSerializer
        return super().get_serializer_class()
