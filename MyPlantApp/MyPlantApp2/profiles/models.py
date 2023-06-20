from django.core.validators import MinLengthValidator
from django.db import models

from profiles.validators import name_validator


class Profile(models.Model):
    username = models.CharField(validators=[MinLengthValidator(2)], max_length=10)
    first_name = models.CharField(validators=[name_validator], max_length=20)
    last_name = models.CharField(validators=[name_validator], max_length=20)
    profile_picture = models.URLField(null=True, blank=True)
