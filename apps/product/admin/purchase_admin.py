from django.contrib import admin

from apps.product.models import Purchase


class PurchaseAdmin(admin.ModelAdmin):
    list_display = ('purchase_id', 'quantity', 'is_closed', 'product', 'supplier', 'created_by')
    list_display_links = ('purchase_id',)
    list_filter = ('is_closed',)
    search_fields = ('purchase_id', 'product__name', 'supplier__name', 'created_by__username')
    list_per_page = 20


admin.site.register(Purchase, PurchaseAdmin)
