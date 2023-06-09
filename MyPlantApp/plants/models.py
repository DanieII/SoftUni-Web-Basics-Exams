from django.core.exceptions import ValidationError
from django.core.validators import MinLengthValidator
from django.db import models


def name_validator(value):
    if not all([x.isalpha() for x in value]):
        raise ValidationError("Plant name should contain only letters!")


class Plant(models.Model):
    PLANT_CHOICES = [
        ('Outdoor Plants', 'Outdoor Plants'),
        ('Indoor Plants', 'Indoor Plants'),
    ]

    plant_type = models.CharField(max_length=14, choices=PLANT_CHOICES, verbose_name='Type')
    name = models.CharField(max_length=20, validators=[MinLengthValidator(2), name_validator])
    image_url = models.URLField(verbose_name='Image URL')
    description = models.TextField()
    price = models.FloatField()
