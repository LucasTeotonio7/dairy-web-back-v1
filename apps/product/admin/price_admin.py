from django.contrib import admin


from apps.product.models import Price


class PriceAdmin(admin.ModelAdmin):
    list_display = ('id', 'value', 'product', 'description', 'created_by')
    list_display_links = ('id',)
    search_fields = ('id', 'product__name', 'description')
    list_per_page = 20


admin.site.register(Price, PriceAdmin)
