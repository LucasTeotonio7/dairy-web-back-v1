from django.contrib import admin

from apps.core.models import Address


class AddressAdmin(admin.ModelAdmin):
    list_display = ('id', 'street', 'city', 'state')
    list_display_links = ('id', )
    search_fields = ('id', 'city', 'state')
    list_per_page = 20


admin.site.register(Address, AddressAdmin)
