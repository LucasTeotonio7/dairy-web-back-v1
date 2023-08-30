import uuid

from django.db import models

from apps.core.models.mixins.timestamped_model import TimestampedModel
from apps.core.models import User
from apps.product.models import Product


class Price(TimestampedModel):
    price_id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    value = models.DecimalField(max_digits=8, decimal_places=2)
    description = models.CharField(max_length=50, blank=True, null=True)
    default = models.BooleanField(default=False)
    product = models.ForeignKey(Product, on_delete=models.PROTECT)
    created_by = models.ForeignKey(User, on_delete=models.PROTECT)

    class Meta:
        db_table = 'price'
        ordering = ['created_at']
        verbose_name = 'Price'
        verbose_name_plural = 'Prices'

    def __str__(self):
        return f'{self.description} {self.product} {self.value}'
