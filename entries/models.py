from django.db import models


class Entry(models.Model):
    name = models.CharField(max_length=100)
    template = models.TextField(blank=True)

    class Meta:
        verbose_name_plural = "Entries"

    def __str__(self):
        return self.name

class Metadata(models.Model):
    entry = models.ForeignKey(Entry)
    name = models.CharField(max_length=100)
    key = models.CharField(max_length=50)
    required = models.BooleanField(default=True)

    class Meta:
        verbose_name_plural = "metadata"

    def __str__(self):
        return "{} - {}".format(name, key)
