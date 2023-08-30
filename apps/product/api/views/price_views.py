from rest_framework import viewsets

from apps.product.models import Price
from apps.product.api.serializers.price_serializer import PriceSerializer


class PriceView(viewsets.ModelViewSet):
    queryset = Price.objects.all()
    serializer_class = PriceSerializer
