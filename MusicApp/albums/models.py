from django.core.validators import MinValueValidator
from django.db import models


class Album(models.Model):
    CHOICES = (
        ('pop', 'Pop Music'),
        ('jazz', 'Jazz Music'),
        ('rnb', 'R&B Music'),
        ('rock', 'Rock Music'),
        ('country', 'Country Music'),
        ('dance', 'Dance Music'),
        ('hiphop', 'Hip Hop Music'),
        ('other', 'Other'),
    )
    album_name = models.CharField(unique=True, max_length=30)
    artist = models.CharField(max_length=30)
    genre = models.CharField(max_length=30, choices=CHOICES)
    description = models.TextField(blank=True, null=True)
    image_url = models.URLField()
    price = models.FloatField(validators=[MinValueValidator(0)])
