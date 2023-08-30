from rest_framework import viewsets

from apps.product.models import Product
from apps.product.api.serializers.product_serializers import ProductSerializer


class ProductView(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
