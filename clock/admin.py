from django.contrib import admin
from clock import models


@admin.register(models.Clock)
class ClockAdmin(admin.ModelAdmin):
    list_display = ['created_by', 'check_in', 'check_out']
    search_fields = ['created_by', 'check_in', 'check_out']
    list_filter = ['created_by']
