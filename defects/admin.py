from django.contrib import admin

from defects.models import Defect


@admin.register(Defect)
class DefectAdmin(admin.ModelAdmin):
    list_display = ('pk', 'user', 'title', 'body', 'status', 'created_at')
    list_filter = ('user', 'status')
    search_fields = ('user', 'status')
    empty_value_display = '-пусто-'
