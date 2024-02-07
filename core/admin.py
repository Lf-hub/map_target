from django.contrib import admin

from core.models import Target


# Register your models here.

class TargetAdmin(admin.ModelAdmin):
    search_fields = ['name']
    list_filter = ['name']
    list_display = ['name', 'latitude', 'longitude', 'expiration_date']

admin.site.register(Target, TargetAdmin)