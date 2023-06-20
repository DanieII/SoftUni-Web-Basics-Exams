from django.core.validators import MinLengthValidator
from django.db import models

from plants.validators import name_validator


class Plant(models.Model):
    PLANT_TYPE_CHOICES = [
        ('Outdoor Plants', 'Outdoor Plants'),
        ('Indoor Plants', 'Indoor Plants')
    ]
    plant_type = models.CharField(choices=PLANT_TYPE_CHOICES, max_length=14)
    name = models.CharField(validators=[MinLengthValidator(2), name_validator], max_length=20)
    image_url = models.URLField()
    description = models.TextField()
    price = models.FloatField()
