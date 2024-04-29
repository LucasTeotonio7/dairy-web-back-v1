import uuid

from django.db import models

from apps.core.models.mixins.timestamped_model import TimestampedModel
from apps.core.models import Supplier
from apps.product.models import WeeklyControl


class SupplierPayment(TimestampedModel):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    quantity = models.DecimalField(max_digits=8, decimal_places=2)
    unit_price = models.DecimalField(max_digits=8, decimal_places=2)
    supplier = models.ForeignKey(Supplier, on_delete=models.PROTECT)
    weekly_control = models.ForeignKey(WeeklyControl, on_delete=models.PROTECT)

    class Meta:
        db_table = 'supplier_payment'
        ordering = ['created_at']
        verbose_name = 'Supplier payment'
        verbose_name_plural = 'Supplier payments'
        constraints = [
            models.UniqueConstraint(fields=['supplier', 'weekly_control'], name='unique_weekly_supplier_payment'),
        ]

    def __str__(self):
        return f'{self.weekly_control} {self.quantity} {self.unit_price}'
