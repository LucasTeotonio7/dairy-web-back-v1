import uuid

from django.db import models

from apps.core.models.mixins.timestamped_model import TimestampedModel
from apps.core.models import User, Supplier
from apps.product.models import WeeklyControl


class WeeklyControlEvent(TimestampedModel):

    class Type(models.TextChoices):
        RECORD = 'RECORD', 'Registro'
        PAYMENT = 'PAYMENT', 'Pagamento'
        PRICE = 'PRICE', 'Preço'

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    type = models.CharField(max_length=7, choices=Type.choices)
    description = models.CharField(max_length=255, blank=True, null=True)
    supplier = models.ForeignKey(Supplier, on_delete=models.PROTECT)
    weekly_control = models.ForeignKey(WeeklyControl, on_delete=models.PROTECT)
    created_by = models.ForeignKey(User, on_delete=models.PROTECT)

    class Meta:
        db_table = 'weekly_control_event'
        ordering = ['created_at']
        verbose_name = 'Weekly control event'
        verbose_name_plural = 'Weekly control events'

    def __str__(self):
        return f'{self.description} {self.supplier} {self.created_by}'
