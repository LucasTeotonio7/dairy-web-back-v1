from datetime import timedelta

from apps.core.models import Supplier
from apps.product.models import Purchase, WeeklyControl


def get_weekly_control_purchases_by_supplier(week_control: WeeklyControl):

    start_date = week_control.start_date
    end_date = week_control.end_date
    product = week_control.product

    date_range = [start_date + timedelta(days=i) for i in range((end_date - start_date).days + 1)]

    result = []
    suppliers = Supplier.objects.all()
    for supplier in suppliers:
        purchases_by_supplier = Purchase.objects.filter(
            reference_day__gte=start_date,
            reference_day__lte=end_date,
            product=product,
            supplier=supplier
        )
        purchases = []
        total_quantity = 0.00
        for date in date_range:
            quantity = 0.00
            purchase_by_reference_day = purchases_by_supplier.filter(reference_day=date).first()
            if purchase_by_reference_day:
                quantity = purchase_by_reference_day.quantity
            purchases.append({
                'reference_day': date.strftime('%Y-%m-%d'),
                'quantity':  quantity,
                'weekday': date.weekday()
            })
            total_quantity += float(quantity)

        result.append({
            'supplier': supplier.name,
            'purchases': purchases,
            'total_quantity': total_quantity
        })

    return result
