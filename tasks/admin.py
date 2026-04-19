from django.contrib import admin
from .models import Task


@admin.register(Task)
class TaskAdmin(admin.ModelAdmin):
    list_display = (
        'title',
        'lead',
        'deal',
        'assigned_to',
        'due_date',
        'due_time',
        'status',
        'priority',
        'created_at',
    )
    list_filter = ('status', 'priority', 'due_date', 'assigned_to')
    search_fields = ('title', 'lead__name', 'deal__title', 'notes')
    ordering = ('due_date', 'due_time')