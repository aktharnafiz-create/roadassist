from django.contrib import admin
from django.utils.html import format_html
from .models import Workshop, BreakdownRequest


@admin.register(Workshop)
class WorkshopAdmin(admin.ModelAdmin):
    list_display = ('name', 'phone', 'area')


@admin.register(BreakdownRequest)
class BreakdownRequestAdmin(admin.ModelAdmin):
    list_display = ('customer_name', 'phone', 'problem', 'created_at', 'map_link')
    list_filter = ('problem', 'created_at')

    def map_link(self, obj):
        if obj.latitude and obj.longitude:
            url = f"https://www.google.com/maps?q={obj.latitude},{obj.longitude}"
            return format_html('<a href="{}" target="_blank">Open in Maps</a>', url)
        return "No location"

    map_link.short_description = "Location"