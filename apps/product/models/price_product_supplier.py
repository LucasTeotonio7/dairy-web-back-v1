import uuid

from django.db import models

from apps.core.models.mixins.timestamped_model import TimestampedModel
from apps.core.models import Supplier
from apps.product.models import Price


class PriceProductSupplier(TimestampedModel):
    price_product_supplier_id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    price = models.ForeignKey(Price, on_delete=models.PROTECT)
    supplier = models.ForeignKey(Supplier, on_delete=models.PROTECT)

    class Meta:
        db_table = 'price_product_supplier'
        ordering = ['created_at']
        verbose_name = 'Price product supplier'
        verbose_name_plural = 'Product supplier pricing'

    def __str__(self):
        return f'{self.price} {self.supplier}'
