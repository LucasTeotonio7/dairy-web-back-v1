from django.contrib import admin

from apps.product.models import Brand


class BrandAdmin(admin.ModelAdmin):
    list_display = ('brand_id', 'description')
    list_display_links = ('brand_id', )
    search_fields = ('description', )
    list_per_page = 20


admin.site.register(Brand, BrandAdmin)
