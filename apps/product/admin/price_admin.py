from django.contrib import admin


from apps.product.models import Price


class PriceAdmin(admin.ModelAdmin):
    list_display = ('price_id', 'value', 'product', 'description', 'created_by')
    list_display_links = ('price_id',)
    search_fields = ('price_id', 'product__name', 'description')
    list_per_page = 20


admin.site.register(Price, PriceAdmin)
