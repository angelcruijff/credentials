from django.contrib import admin
from .models import Entry, Metadata

class EntryAdmin(admin.ModelAdmin):
    empty_value_display = '-Select-'


class MetadataAdmin(admin.ModelAdmin):
    empty_value_display = '-Select-'
    list_display = ('entry', 'name', 'key', 'required')


admin.site.register(Entry, EntryAdmin)
admin.site.register(Metadata, MetadataAdmin)
