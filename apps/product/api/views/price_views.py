from drf_spectacular.utils import extend_schema
from rest_framework.response import Response
from rest_framework import viewsets
from rest_framework import status

from apps.core.components import Paginator
from apps.product.models import Price, PriceProductSupplier, WeeklyControl, WeeklyControlEvent
from apps.product.api.serializers.price_serializers import PriceSerializer, PriceProductSupplierSerializer


@extend_schema(tags=['Price', ])
class PriceView(viewsets.ModelViewSet):
    queryset = Price.objects.all()
    serializer_class = PriceSerializer
    pagination_class = Paginator

    def get_queryset(self):
        queryset = super().get_queryset()

        product_id = self.request.query_params.get('product_id', None)
        if product_id:
            queryset = queryset.filter(product_id=product_id)

        no_pagination = self.request.query_params.get('no_paginate', None)
        if no_pagination:
            self.pagination_class = None
        else:
            self.pagination_class = Paginator
        return queryset

    def destroy(self, request, pk):
        price: Price = self.get_object()
        if price.default:
            product = price.product
            weekly_control_exists = WeeklyControl.objects.filter(product=product).exists()
            if weekly_control_exists:
                return Response(
                    data={'message': 'Products with a spreadsheet must have at least one default table.'},
                    status=status.HTTP_403_FORBIDDEN
                )

        price_product_supplier_list = PriceProductSupplier.objects.filter(price=price)
        for price_ps in price_product_supplier_list:
            price_default = Price.objects.filter(default=True, product=price_ps.price.product).first()
            weekly_control_list = WeeklyControl.objects.filter(product=price_default.product, is_closed=False)
            for weekly_control in weekly_control_list:
                weekly_control_event = WeeklyControlEvent(
                    type=WeeklyControlEvent.Type.PRICE,
                    new_value=price_default.value,
                    old_value=price_ps.price.value,
                    supplier=price_ps.supplier,
                    description=f'A tabela <b>{ price_ps.price.description } R$ { price_ps.price.value }</b> foi excluída.',
                    weekly_control=weekly_control,
                    created_by=self.request.user
                )
                weekly_control_event.save()
            price_ps.delete()

        return super().destroy(request, pk)


@extend_schema(tags=['Price Product Supplier', ])
class PriceProductSupplierView(viewsets.ModelViewSet):
    queryset = PriceProductSupplier.objects.all()
    serializer_class = PriceProductSupplierSerializer


    def destroy(self, request, pk):
        try:
            instance: PriceProductSupplier = self.get_object()
            weekly_control_event = WeeklyControlEvent(
                type=WeeklyControlEvent.Type.PRICE,
                old_value=instance.price.value,
                new_value=request.query_params.get('new_value'),
                supplier=instance.supplier,
                weekly_control_id=request.query_params.get('weekly_control_id'),
                created_by=request.user
            )
            weekly_control_event.save()
            instance.hard_delete()
            return Response(status=status.HTTP_204_NO_CONTENT)

        except PriceProductSupplierSerializer.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
