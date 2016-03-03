from django.contrib import admin
from .models import Entry, Metadata, MetadataValue, EntryType

class EntryTypeAdmin(admin.ModelAdmin):
    empty_value_display = '-Select-'

class EntryAdmin(admin.ModelAdmin):
    empty_value_display = '-Select-'


class MetadataAdmin(admin.ModelAdmin):
    empty_value_display = '-Select-'
    list_display = ('entry_type', 'name', 'key', 'required')

class MetadataValueAdmin(admin.ModelAdmin):
    list_display = ('entry', 'metadata','value')


admin.site.register(EntryType, EntryTypeAdmin)
admin.site.register(Entry, EntryAdmin)
admin.site.register(Metadata, MetadataAdmin)
admin.site.register(MetadataValue, MetadataValueAdmin)
