from django.contrib import admin

from apps.product.models import MeasureUnit


class MeasureUnitAdmin(admin.ModelAdmin):
    list_display = ('measure_unit_id', 'abbreviation', 'description')
    list_display_links = ('measure_unit_id', )
    search_fields = ('abbreviation', 'description')
    list_per_page = 20


admin.site.register(MeasureUnit, MeasureUnitAdmin)
