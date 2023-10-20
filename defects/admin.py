from django.contrib import admin

from defects.models import Defect


@admin.register(Defect)
class DefectAdmin(admin.ModelAdmin):
    list_display = (
        'pk',
        'user',
        'title',
        'body',
        'status',
        'department',
        'created_at',
    )
    list_filter = ('user', 'status', 'department')
    search_fields = ('user', 'status', 'department')
    empty_value_display = '-пусто-'
