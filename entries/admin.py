from django.contrib import admin
from .models import Entry, Metadata

admin.site.register(Entry, Metadata)
