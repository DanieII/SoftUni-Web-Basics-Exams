from django.core.validators import MinLengthValidator
from django.db import models

from pets.models import Pet
from photos.validators import image_size_validator


class Photo(models.Model):
    photo = models.ImageField(validators=[image_size_validator])
    description = models.TextField(max_length=300, validators=[MinLengthValidator(10)], null=True, blank=True)
    location = models.CharField(max_length=30)
    tagged_pets = models.ManyToManyField(Pet, blank=True)
    date_of_publication = models.DateTimeField(auto_now=True)
