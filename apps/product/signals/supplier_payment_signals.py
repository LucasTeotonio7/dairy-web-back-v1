from django.db.models.signals import post_save
from django.dispatch import receiver

from apps.product.models import SupplierPayment
from apps.core.models import Supplier


@receiver(post_save, sender=SupplierPayment)
def company_sync(instance: SupplierPayment, created, **kwargs):
    weekly_control = instance.weekly_control
    active_suppliers = Supplier.objects.filter(active=True)
    suppliers_paid = SupplierPayment.objects.filter(
        weekly_control=weekly_control, supplier__in=active_suppliers
    )

    if active_suppliers.count() == suppliers_paid.count():
        weekly_control.is_closed = True
        weekly_control.save()
