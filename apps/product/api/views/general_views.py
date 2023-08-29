from rest_framework import viewsets

from apps.product.models import MeasureUnit, Category, Brand
from apps.product.api.serializers.general_serializers import (
    MeasureUnitSerializer, CategorySerializer, BrandSerializer
)


class MeasureUnitView(viewsets.ModelViewSet):
    queryset = MeasureUnit.objects.all()
    serializer_class = MeasureUnitSerializer
    http_method_names = ['get', 'post', 'put', 'patch', 'delete']
 

class CategoryView(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    http_method_names = ['get', 'post', 'put', 'delete']


class BrandView(viewsets.ModelViewSet):
    queryset = Brand.objects.all()
    serializer_class = BrandSerializer
    http_method_names = ['get', 'post', 'put', 'delete']
