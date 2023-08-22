from django.contrib import admin

from apps.core.models import User


class UserAdmin(admin.ModelAdmin):
    list_display = ('user_id', 'name', 'last_name', 'username', 'email', 'is_active')
    list_display_links = ('user_id', )
    search_fields = ('user_id', 'name', 'username')
    list_per_page = 20


admin.site.register(User, UserAdmin)
