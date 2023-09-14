from drf_spectacular.utils import extend_schema
from rest_framework import viewsets

from apps.product.models import Product
from apps.product.api.serializers.product_serializers import ProductSerializer


@extend_schema(tags=['Product', ])
class ProductView(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
