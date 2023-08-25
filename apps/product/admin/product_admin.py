from django.contrib import admin

from apps.product.models import Product


class ProductAdmin(admin.ModelAdmin):
    list_display = ('product_id', 'description', 'brand', 'category', 'measure_unit', 'active')
    list_display_links = ('product_id', )
    search_fields = ('product_id', 'description', )
    list_per_page = 20


admin.site.register(Product, ProductAdmin)
