from django.core.exceptions import ValidationError
from django.core.validators import MinLengthValidator
from django.db import models


def name_validator(value):
    if not value[0].isupper():
        raise ValidationError("Your name must start with a capital letter!")


class Profile(models.Model):
    username = models.CharField(max_length=10, validators=[MinLengthValidator(2)])
    first_name = models.CharField(max_length=20, validators=[name_validator])
    last_name = models.CharField(max_length=20, validators=[name_validator])
    profile_picture = models.URLField(blank=True, null=True)
