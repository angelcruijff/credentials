from django.db import models


class Entry(models.Model):
    name = models.CharField(max_length=100)
    template = models.TextField(blank=True)

class Metadata(models.Model):
    entry = models.ForeigKey(Entry)
    name = models.CharField(max_length=100)
    key = models.CharField(max_length=50)
    required = models.BooleanField(default=True)
