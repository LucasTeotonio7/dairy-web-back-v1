from django.contrib import admin

from apps.product.models import PriceProductSupplier


class PriceProductSupplierAdmin(admin.ModelAdmin):
    list_display = ('id', 'price', 'supplier')
    list_display_links = ('id',)
    search_fields = ('id', 'price__value', 'supplier__name')
    list_per_page = 20


admin.site.register(PriceProductSupplier, PriceProductSupplierAdmin)
