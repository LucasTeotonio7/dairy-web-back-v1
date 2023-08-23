import uuid

from django.db import models

from apps.core.models.mixins.timestamped_model import TimestampedModel


class MeasureUnit(TimestampedModel):
    measure_unit_id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    description = models.CharField(max_length=50, blank=False, unique=True)
    abbreviation = models.CharField(max_length=3, blank=False, unique=True)

    class Meta:
        db_table = 'measure_unit'
        ordering = ['created_at']
        verbose_name = 'Measure unit'
        verbose_name_plural = 'Measurement units'

    def __str__(self):
        return f"{self.abbreviation}, {self.description}"
