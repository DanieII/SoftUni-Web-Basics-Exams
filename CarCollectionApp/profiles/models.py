from django.core.validators import MinValueValidator, MinLengthValidator
from django.db import models


class Profile(models.Model):
    username = models.CharField(max_length=10, validators=[MinLengthValidator(2, "The username must be a minimum of 2 chars")])
    email = models.EmailField()
    age = models.IntegerField(validators=[MinValueValidator(18)])
    password = models.CharField(max_length=30)
    first_name = models.CharField(blank=True, null=True, max_length=30)
    last_name = models.CharField(blank=True, null=True, max_length=30)
    profile_picture = models.URLField(blank=True, null=True)
