import uuid

from django.db import models

from apps.core.models.mixins.timestamped_model import TimestampedModel
from apps.core.models import User
from apps.product.models import Product


class WeeklyControl(TimestampedModel):
    weekly_control_id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    start_date = models.DateField()
    end_date = models.DateField()
    is_closed = models.BooleanField(default=False)
    product = models.ForeignKey(Product, on_delete=models.PROTECT)
    created_by = models.ForeignKey(User, on_delete=models.PROTECT)

    class Meta:
        db_table = 'weekly_control'
        ordering = ['created_at']
        verbose_name = 'Weekly control'
        verbose_name_plural = 'Weekly controls'

    def __str__(self):
        return f'{self.start_date} {self.end_date}'
