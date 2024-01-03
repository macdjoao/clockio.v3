from django.contrib import admin
from users import models


@admin.register(models.Profile)
class ProfileAdmin(admin.ModelAdmin):
    list_display = ['user', 'role', 'document']
    search_fields = ['user', 'role', 'document']
    list_filter = ['role']
