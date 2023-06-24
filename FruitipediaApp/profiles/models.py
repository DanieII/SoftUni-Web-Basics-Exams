from django.core.validators import MinLengthValidator
from django.db import models

from profiles.validators import name_validator


class Profile(models.Model):
    first_name = models.CharField(max_length=25, validators=[MinLengthValidator(2), name_validator])
    last_name = models.CharField(max_length=35, validators=[MinLengthValidator(1), name_validator])
    email = models.EmailField(max_length=40)
    password = models.CharField(max_length=20, validators=[MinLengthValidator(8)])
    image_url = models.URLField(null=True, blank=True)
    age = models.IntegerField(null=True, blank=True, default=18)
