from django.db import models


class Audio(models.Model):
    received = models.DateTimeField(auto_now_add=True)
    ts = models.DateTimeField()
    session_id = models.CharField(max_length=100, blank=True, default='')

    class Meta:
        ordering = ['received']
