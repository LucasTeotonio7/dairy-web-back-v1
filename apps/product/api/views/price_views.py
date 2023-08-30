from rest_framework.response import Response
from rest_framework import viewsets
from rest_framework import status

from apps.product.models import Price, PriceProductSupplier
from apps.product.api.serializers.price_serializers import PriceSerializer, PriceProductSupplierSerializer


class PriceView(viewsets.ModelViewSet):
    queryset = Price.objects.all()
    serializer_class = PriceSerializer


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
