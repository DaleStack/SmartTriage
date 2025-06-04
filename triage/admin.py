from django.contrib import admin
from .models import TriageModel
from django.utils.timezone import localtime
# Register your models here.

class TriageAdmin(admin.ModelAdmin):
    list_display = ('full_name', 'localized_submitted_at', 'reviewed', 'assigned_doctor')

    def localized_submitted_at(self, obj):
        return localtime(obj.submitted_at).strftime('%Y-%m-%d %I:%M %p')  # 12-hour format
    localized_submitted_at.short_description = 'Submitted At (Asia/Manila)'

admin.site.register(TriageModel, TriageAdmin)