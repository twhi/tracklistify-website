from django.contrib import admin
from .models import Usage

@admin.register(Usage)
class UsageAdmin(admin.ModelAdmin):
    readonly_fields = ('updated',)
