from django.contrib import admin
from .models import Deal


@admin.register(Deal)
class DealAdmin(admin.ModelAdmin):
    list_display = ('title', 'lead', 'value', 'stage', 'expected_close_date', 'created_at')
    list_filter = ('stage', 'created_at', 'expected_close_date')
    search_fields = ('title', 'lead__name')