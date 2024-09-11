from datetime import timedelta

from django.db.models import F, Sum
from django.db.models.functions import TruncMonth
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


def get_analysis_by_month():
    MONTH_NAMES_PT_BR = {
        1: 'Janeiro', 2: 'Fevereiro', 3: 'Março', 4: 'Abril', 5: 'Maio', 6: 'Junho',
        7: 'Julho', 8: 'Agosto', 9: 'Setembro', 10: 'Outubro', 11: 'Novembro', 12: 'Dezembro'
    }

    amount_paid_monthly = SupplierPayment.objects.filter(
        created_at__gte=(timezone.now() - timedelta(days=180))
    ).annotate(
        month=TruncMonth('created_at'),
        total_value=F('quantity') * F('unit_price')
    ).values('month').annotate(
        total_value_sum=Sum('total_value')
    ).order_by('month')

    amount_paid_monthly_with_month_name = [
        {
            'month': MONTH_NAMES_PT_BR[entry['month'].month],
            'total': entry['total_value_sum']
        }
        for entry in amount_paid_monthly
    ]

    return amount_paid_monthly_with_month_name


def get_analysis_by_supplier():
    sixty_days_ago = timezone.now() - timedelta(days=60)
    supplier_quantities = SupplierPayment.objects.filter(
        created_at__gte=sixty_days_ago
    ).values('supplier__name').annotate(
        total_quantity=Sum('quantity')
    ).order_by('-total_quantity')[:10]

    result_dict = []
    for entry in supplier_quantities:
        result_dict.append({
            "name" : entry['supplier__name'],
            "value" : float(entry['total_quantity'])
        })

    return result_dict
