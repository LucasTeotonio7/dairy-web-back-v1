from django.contrib import admin

from apps.product.models import Category


class CategoryAdmin(admin.ModelAdmin):
    list_display = ('category_id', 'description')
    list_display_links = ('category_id', )
    search_fields = ('description', )
    list_per_page = 20


admin.site.register(Category, CategoryAdmin)
