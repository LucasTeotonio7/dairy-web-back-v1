from datetime import timedelta

from apps.core.models import Supplier
from apps.product.models import Purchase, WeeklyControl, Price, SupplierPayment


def get_weekly_control_purchases_by_supplier(weekly_control: WeeklyControl, supplier_id: str = None):

    start_date = weekly_control.start_date
    end_date = weekly_control.end_date

    date_range = [start_date + timedelta(days=i) for i in range((end_date - start_date).days + 1)]

    result = []
    suppliers = Supplier.objects.all()
    if supplier_id:
        suppliers = suppliers.filter(id=supplier_id)

    for supplier in suppliers:
        purchases_by_supplier = Purchase.objects.filter(
            weekly_control=weekly_control,
            supplier=supplier
        )
        purchases = []
        total_quantity = 0.00
        for date in date_range:
            quantity = 0.00
            price = 0.00
            id = None
            purchase_by_reference_day = purchases_by_supplier.filter(reference_day=date).first()
            if purchase_by_reference_day:
                quantity = purchase_by_reference_day.quantity
                id = purchase_by_reference_day.id

            purchases.append({
                'id': id,
                'reference_day': date.strftime('%Y-%m-%d'),
                'quantity':  quantity,
                'weekday': date.weekday()
            })
            total_quantity += float(quantity)

        price_table = supplier.priceproductsupplier_set.filter(
            price__product=weekly_control.product
        ).first()
        price = {}
        if not price_table:
            price_default = Price.objects.filter(
                product=weekly_control.product, 
                default=True
            ).first()
            if price_default:
                price['value'] = float(price_default.value)
                price['id'] = price_default.id
                price['default'] = True
        else:
            price['value'] = float(price_table.price.value)
            price['id'] = price_table.price_id
            price['price_product_supplier_id'] = price_table.id
            price['default'] = False
        paid_supplier = SupplierPayment.objects.filter(
            weekly_control=weekly_control,
            supplier=supplier,
        ).exists()
        result.append({
            'id': supplier.id,
            'name': supplier.name,
            'paid_supplier': paid_supplier,
            'price': price,
            'purchases': purchases,
            'total_quantity': total_quantity
        })

    return result
