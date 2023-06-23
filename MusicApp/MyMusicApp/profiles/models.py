from django.core.exceptions import ValidationError
from django.core.validators import MinLengthValidator
from django.db import models


def validate_username(value):
    if not all([x.isalpha() or x.isdigit() or x == "_" for x in value]):
        raise ValidationError("Ensure this value contains only letters, numbers, and underscore.")
    return value


class Profile(models.Model):
    username = models.CharField(max_length=15, validators=[MinLengthValidator(2), validate_username])
    email = models.EmailField()
    age = models.PositiveIntegerField(blank=True, null=True)
