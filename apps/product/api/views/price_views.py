from drf_spectacular.utils import extend_schema
from rest_framework.response import Response
from rest_framework import viewsets
from rest_framework import status

from apps.core.components import Paginator
from apps.product.models import Price, PriceProductSupplier
from apps.product.api.serializers.price_serializers import PriceSerializer, PriceProductSupplierSerializer


@extend_schema(tags=['Price', ])
class PriceView(viewsets.ModelViewSet):
    queryset = Price.objects.all()
    serializer_class = PriceSerializer
    pagination_class = Paginator


@extend_schema(tags=['Price Product Supplier', ])
class PriceProductSupplierView(viewsets.ModelViewSet):
    queryset = PriceProductSupplier.objects.all()
    serializer_class = PriceProductSupplierSerializer


    def destroy(self, request, pk):
        try:
            instance: PriceProductSupplier = self.get_object()
            instance.hard_delete()
            return Response(status=status.HTTP_204_NO_CONTENT)
        
        except PriceProductSupplierSerializer.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
