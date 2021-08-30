from django.db import models
from django.urls import reverse


class Artist(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return f"<Artists: {self.name}>"

    def get_absolute_url(self):
        return reverse('artist-detail')


class Song(models.Model):
    title = models.CharField(max_length=255)
    artist = models.ForeignKey(Artist, on_delete=models.CASCADE)
    votes = models.IntegerField(default=1)

    def __str__(self):
        return f"<Songs: {self.title}>"

    def get_absolute_url(self):
        return reverse('song-detail', args=[str(self.id)])
