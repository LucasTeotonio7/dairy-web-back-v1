from django.contrib import admin

from apps.core.models import Supplier


class SupplierAdmin(admin.ModelAdmin):
    list_display = ('supplier_id', 'name', 'cellphone', 'active')
    list_display_links = ('supplier_id', )
    search_fields = ('name', )
    list_per_page = 20


admin.site.register(Supplier, SupplierAdmin)
