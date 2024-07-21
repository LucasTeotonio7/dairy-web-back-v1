from django.utils import timezone

from django.db import models


class SoftDeletionManager(models.Manager):
    def get_queryset(self):
        return super().get_queryset().filter(deleted=None)


class TimestampedModel(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    deleted = models.DateTimeField(null=True, blank=True)

    objects = SoftDeletionManager()
    dm_objects = models.Manager()
    
    class Meta:
        abstract = True

    def delete(self, using=None, keep_parents=False):
        self.deleted = timezone.now()
        self.save()

    def hard_delete(self):
        super().delete()

    def undelete(self):
        self.deleted = None
        self.save()
