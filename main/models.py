from django.db import models

from urllib.parse import urlparse

# Create your models here.
class Usage(models.Model):
    username = models.CharField(max_length=256)
    show_url = models.CharField(max_length=1000)
    tracks_found = models.IntegerField(default=0)
    total_tracks = models.IntegerField(default=0)

    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        ws = urlparse(self.show_url).netloc
        return '{user} - {site}'.format(user=self.username, site=ws)