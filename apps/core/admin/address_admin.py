from django.contrib import admin

from apps.core.models import Address


class AddressAdmin(admin.ModelAdmin):
    list_display = ('address_id', 'street', 'city', 'state')
    list_display_links = ('address_id', )
    search_fields = ('address_id', 'city', 'state')
    list_per_page = 20


admin.site.register(Address, AddressAdmin)
