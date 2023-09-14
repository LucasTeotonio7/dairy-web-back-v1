from drf_spectacular.utils import extend_schema
from rest_framework import viewsets

from apps.product.models import Purchase
from apps.product.api.serializers.purchase_serializers import PurchaseSerializer


@extend_schema(tags=['Purchase', ])
class PurchaseView(viewsets.ModelViewSet):
    queryset = Purchase.objects.all()
    serializer_class = PurchaseSerializer
