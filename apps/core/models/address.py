import uuid

from django.db import models


class Address(models.Model):
    address_id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    street = models.CharField(max_length=255)
    number = models.CharField(max_length=10, null=True, blank=True)
    zone = models.CharField(max_length=50, null=True, blank=True)
    city = models.CharField(max_length=50)
    state = models.CharField(max_length=2)
    postal_code = models.CharField(max_length=8, null=True, blank=True)
    complement = models.CharField(max_length=100, null=True, blank=True)

    class Meta:
        db_table = 'address'
        ordering = ['street']
        verbose_name = 'Address'
        verbose_name_plural = 'Addresses'

    def __str__(self):
        return f"{self.street}, {self.city}, {self.state}"
