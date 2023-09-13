from django.contrib import admin

from apps.product.models import MeasureUnit


class MeasureUnitAdmin(admin.ModelAdmin):
    list_display = ('id', 'abbreviation', 'description')
    list_display_links = ('id', )
    search_fields = ('abbreviation', 'description')
    list_per_page = 20


admin.site.register(MeasureUnit, MeasureUnitAdmin)
