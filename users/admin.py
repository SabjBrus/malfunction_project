from django.contrib import admin

from users.models import CustomUser, Department


@admin.register(CustomUser)
class CustomUserAdmin(admin.ModelAdmin):
    list_display = (
        'pk',
        'email',
        'first_name',
        'last_name',
        'slug',
        'date_joined',
        'department',
    )
    list_filter = ('slug', 'email')
    search_fields = ('slug', 'email')
    empty_value_display = '-пусто-'


@admin.register(Department)
class DepartmentAdmin(admin.ModelAdmin):
    list_display = ('pk', 'name', 'slug')
    list_filter = ('name', 'slug')
    search_fields = ('name', 'slug')
    empty_value_display = '-пусто-'
