from django.contrib import admin

from apps.product.models import Purchase


class PurchaseAdmin(admin.ModelAdmin):
    list_display = ('id', 'reference_day', 'weekly_control', 'quantity', 'product', 'supplier')
    list_display_links = ('id',)
    search_fields = ('id', 'product__name', 'supplier__name')
    list_per_page = 20


admin.site.register(Purchase, PurchaseAdmin)
