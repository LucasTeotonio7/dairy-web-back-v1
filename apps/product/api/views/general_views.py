from drf_spectacular.utils import extend_schema
from rest_framework import viewsets

from apps.product.models import MeasureUnit, Category, Brand
from apps.product.api.serializers.general_serializers import (
    MeasureUnitSerializer, CategorySerializer, BrandSerializer
)


@extend_schema(tags=['Measure Unit', ])
class MeasureUnitView(viewsets.ModelViewSet):
    queryset = MeasureUnit.objects.all()
    serializer_class = MeasureUnitSerializer
    http_method_names = ['get', 'post', 'put', 'patch', 'delete']
 

@extend_schema(tags=['Category', ])
class CategoryView(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    http_method_names = ['get', 'post', 'put', 'delete']


@extend_schema(tags=['Brand', ])
class BrandView(viewsets.ModelViewSet):
    queryset = Brand.objects.all()
    serializer_class = BrandSerializer
    http_method_names = ['get', 'post', 'put', 'delete']
