from django.db import models


class EntryType(models.Model):
    name = models.CharField(max_length=100)
    template = models.TextField(blank=True)

    class Meta:
        verbose_name_plural = "Entries Type"

    def __str__(self):
        return self.name


class Metadata(models.Model):
    entry_type = models.ForeignKey(EntryType, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    key = models.CharField(max_length=50)
    required = models.BooleanField(default=True)

    class Meta:
        verbose_name_plural = "Metadata"

    def __str__(self):
        return "{} - {}".format(self.name, self.key)


class Entry(models.Model):
    entry_type = models.ForeignKey(EntryType, on_delete=models.CASCADE)
    name = models.CharField(max_length=100, blank=False)

    class Meta:
        verbose_name_plural = "Entries"

    def __str__(self):
        return self.name


class MetadataValue(models.Model):
    entry = models.ForeignKey(Entry, on_delete=models.CASCADE)
    metadata = models.ForeignKey(Metadata, on_delete=models.CASCADE)
    value = models.CharField(max_length=255)

    def __str__(self):
        return self.value
