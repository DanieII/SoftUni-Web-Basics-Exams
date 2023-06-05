from django.core.exceptions import ValidationError
from django.core.validators import MinValueValidator, MinLengthValidator
from django.db import models


def car_year_validator(value):
    if not 1980 <= value <= 2049:
        raise ValidationError("Year must be between 1980 and 2049")


class Car(models.Model):
    CAR_CHOICES = (
        ('Sports Car', 'Sports Car'),
        ('Pickup', 'Pickup'),
        ('Crossover', 'Crossover'),
        ('Minibus', 'Minibus'),
        ('Other', 'Other')
    )

    type = models.CharField(choices=CAR_CHOICES, max_length=10)
    model = models.CharField(max_length=20, validators=[MinLengthValidator(2)])
    year = models.IntegerField(validators=[car_year_validator])
    image_url = models.URLField()
    price = models.FloatField(validators=[MinValueValidator(1)])
