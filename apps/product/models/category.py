import uuid

from django.db import models

from apps.core.models.mixins.timestamped_model import TimestampedModel


class Category(TimestampedModel):
    category_id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    description = models.CharField(max_length=50, unique=True)

    class Meta:
        db_table = 'category'
        ordering = ['created_at']
        verbose_name = 'Category'
        verbose_name_plural = 'Categories'

    def __str__(self):
        return self.description
