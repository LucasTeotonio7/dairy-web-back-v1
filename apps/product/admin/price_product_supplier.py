from django.contrib import admin

from apps.product.models import PriceProductSupplier


class PriceProductSupplierAdmin(admin.ModelAdmin):
    list_display = ('price_product_supplier_id', 'price', 'supplier')
    list_display_links = ('price_product_supplier_id',)
    search_fields = ('price_product_supplier_id', 'price__value', 'supplier__name')
    list_per_page = 20


admin.site.register(PriceProductSupplier, PriceProductSupplierAdmin)
