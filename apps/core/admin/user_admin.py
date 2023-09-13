from django.contrib import admin

from apps.core.models import User


class UserAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'last_name', 'username', 'email', 'is_active')
    list_display_links = ('id', )
    search_fields = ('id', 'name', 'username')
    list_per_page = 20


admin.site.register(User, UserAdmin)
