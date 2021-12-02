from django.contrib import admin
from.models import Record


class RecordAdmin(admin.ModelAdmin):
    list_display = ('sender', 'particulars', 'office', 'receiver', 'date')

admin.site.register(Record, RecordAdmin)