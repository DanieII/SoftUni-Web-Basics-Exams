from django.core.validators import MinLengthValidator
from django.db import models

from fruits.validators import name_validator


class Fruit(models.Model):
    name = models.CharField(max_length=30, validators=[MinLengthValidator(2), name_validator])
    image_url = models.URLField()
    description = models.TextField()
    nutrition = models.TextField(null=True, blank=True)

    class Meta:
        ordering = ['pk']
