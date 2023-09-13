from django.contrib import admin

from apps.product.models import WeeklyControl


class WeeklyControlAdmin(admin.ModelAdmin):
    list_display = ('id', 'start_date', 'end_date', 'is_closed', 'product', 'created_by')
    list_display_links = ('id',)
    list_filter = ('is_closed', 'product')
    search_fields = ('id', 'start_date', 'end_date', 'product__name', 'created_by__username')
    list_per_page = 20


admin.site.register(WeeklyControl, WeeklyControlAdmin)
