from drf_spectacular.utils import extend_schema
from rest_framework import viewsets

from apps.core.components import Paginator
from apps.product.models import Product, Price
from apps.product.api.serializers.product_serializers import ProductSerializer, ProductDetailSerializer


@extend_schema(tags=['Product', ])
class ProductView(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    pagination_class = Paginator

    def get_queryset(self):
        queryset = super().get_queryset()
        no_pagination = self.request.query_params.get('no_paginate', None)
        default_table = self.request.query_params.get('default_table')
        if no_pagination:
            self.pagination_class = None
        if default_table:
            product_ids = Price.objects.filter(
                product__in=queryset, default=True
            ).values_list('product', flat=True)
            queryset = queryset.filter(pk__in=product_ids)
        else:
            self.pagination_class = Paginator
        return queryset

    def get_serializer_class(self):
        if self.action in ['list', 'retrieve']:
            return ProductDetailSerializer
        return super().get_serializer_class()
