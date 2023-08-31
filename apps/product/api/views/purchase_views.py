from rest_framework import viewsets

from apps.product.models import Purchase
from apps.product.api.serializers.purchase_serializers import PurchaseSerializer


class PurchaseView(viewsets.ModelViewSet):
    queryset = Purchase.objects.all()
    serializer_class = PurchaseSerializer
