from django.contrib import admin

from apps.product.models import Product


class ProductAdmin(admin.ModelAdmin):
    list_display = ('id', 'description', 'brand', 'category', 'measure_unit', 'active')
    list_display_links = ('id', )
    search_fields = ('id', 'description', )
    list_per_page = 20


admin.site.register(Product, ProductAdmin)
