from django.contrib import admin
from clock import models


@admin.register(models.Clock)
class ClockAdmin(admin.ModelAdmin):
    list_display = ['user', 'check_in_hour', 'check_out_hour']
    search_fields = ['user', 'check_in_date', 'check_out_date']
    list_filter = ['user']
