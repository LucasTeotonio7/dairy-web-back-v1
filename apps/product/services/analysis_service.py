from datetime import timedelta

from django.db.models import F, Sum
from django.utils import timezone

from apps.core.models import Supplier
from apps.product.models import WeeklyControl, SupplierPayment


def get_analysis_big_numbers():
    amount_paid_weekly = SupplierPayment.objects.filter(
        created_at__gte=(timezone.now() - timedelta(days=7))
    ).annotate(
        total_value=F('quantity') * F('unit_price')
    ).aggregate(Sum('total_value'))

    amount_paid_monthly = SupplierPayment.objects.filter(
        created_at__gte=(timezone.now() - timedelta(days=30))
    ).annotate(
        total_value=F('quantity') * F('unit_price')
    ).aggregate(Sum('total_value'))

    active_suppliers = Supplier.objects.filter(active=True).count()
    weekly_control_active = WeeklyControl.objects.filter(is_closed=False)

    pending_payments = 0
    percentage = 0
    for weekly_control in weekly_control_active:
        payment_count = SupplierPayment.objects.filter(weekly_control=weekly_control).count()
        pending_payments += active_suppliers - payment_count
        percentage += (payment_count * 100) / active_suppliers

    percentage = percentage / weekly_control_active.count()

    data = {
        "amount_paid_weekly" : amount_paid_weekly['total_value__sum'] or 0.0,
        "amount_paid_monthly" : amount_paid_monthly['total_value__sum'] or 0.0,
        "pending_payments": pending_payments,
        "percentage": percentage,
    }
    return data
