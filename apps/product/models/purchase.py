import uuid

from django.db import models

from apps.core.models.mixins.timestamped_model import TimestampedModel
from apps.core.models import User, Supplier
from apps.product.models import Product


class Purchase(TimestampedModel):
    purchase_id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    quantity = models.DecimalField(max_digits=8, decimal_places=2)
    is_closed = models.BooleanField(default=False)
    product = models.ForeignKey(Product, on_delete=models.PROTECT)
    supplier = models.ForeignKey(Supplier, on_delete=models.PROTECT)
    created_by = models.ForeignKey(User, on_delete=models.PROTECT)

    class Meta:
        db_table = 'purchase'
        ordering = ['created_at']
        verbose_name = 'Purchase'
        verbose_name_plural = 'Purchases'

    def __str__(self):
        return f'{self.product} {self.quantity}'
