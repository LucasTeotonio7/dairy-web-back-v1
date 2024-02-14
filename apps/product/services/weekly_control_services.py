from datetime import timedelta
from decimal import Decimal

from django.db.models import Sum, Q, DecimalField
from django.db.models.functions import Coalesce

from apps.core.models import Supplier
from apps.product.models import WeeklyControl


def get_weekly_control_purchases_by_supplier(week_control: WeeklyControl):

    start_date = week_control.start_date
    end_date = week_control.end_date
    product = week_control.product

    date_range = [end_date - timedelta(days=i) for i in range(7)]

    suppliers_with_purchases = Supplier.objects.annotate(
        purchases=Coalesce(
            Sum('purchase__quantity', filter=(
                Q(purchase__reference_day__gte=start_date) &
                Q(purchase__reference_day__lte=end_date) &
                Q(purchase__product=product)
            )),
            Decimal('0.00'), output_field=DecimalField()
        )
    ).values('id', 'name', 'purchases')

    result = []
    for supplier in suppliers_with_purchases:
        purchases = [
            {
                'reference_day': date.strftime('%Y-%m-%d'),
                'quantity': supplier['purchases'] if date in date_range else '0.00',
                'supplier': supplier['name']
            }
            for date in date_range
        ]
        result.append({
            'supplier': supplier['name'],
            'purchases': purchases
        })

    return result
