import uuid

from django.db import models

from apps.core.models.mixins.timestamped_model import TimestampedModel
from apps.core.models import User
from apps.product.models import Brand, Category, MeasureUnit


class Product(TimestampedModel):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    description = models.CharField(max_length=255, blank=True, null=True)
    brand = models.ForeignKey(Brand, on_delete=models.PROTECT)
    category = models.ForeignKey(Category, on_delete=models.PROTECT)
    measure_unit = models.ForeignKey(MeasureUnit, on_delete=models.PROTECT)
    unit_quantity = models.DecimalField(decimal_places=2, max_digits=8, default=1)
    active = models.BooleanField(default=True)
    created_by = models.ForeignKey(User, on_delete=models.PROTECT)
    image = models.ImageField(upload_to='products/', max_length=255, null=True, blank=True)

    class Meta:
        db_table = 'product'
        ordering = ['created_at']
        verbose_name = 'Product'
        verbose_name_plural = 'Products'

    def __str__(self):
        return f'{self.description} {self.brand}'
