from drf_spectacular.utils import extend_schema
from rest_framework import viewsets

from apps.core.components import Paginator
from apps.product.models import Product
from apps.product.api.serializers.product_serializers import ProductSerializer, ProductDetailSerializer


@extend_schema(tags=['Product', ])
class ProductView(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    pagination_class = Paginator

    def get_queryset(self):
        no_pagination = self.request.query_params.get('no_paginate', None)
        if no_pagination:
            self.pagination_class = None
        else:
            self.pagination_class = Paginator
        return super().get_queryset()

    def get_serializer_class(self):
        if self.action in ['list', 'retrieve']:
            return ProductDetailSerializer
        return super().get_serializer_class()
