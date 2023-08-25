import uuid

from django.db import models

from apps.core.models.mixins.timestamped_model import TimestampedModel


class Brand(TimestampedModel):
    brand_id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    description = models.CharField(max_length=50, unique=True)

    class Meta:
        db_table = 'brand'
        ordering = ['created_at']
        verbose_name = 'Brand'
        verbose_name_plural = 'Brands'

    def __str__(self):
        return self.description
