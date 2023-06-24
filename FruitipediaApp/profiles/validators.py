from django.core import exceptions


def name_validator(value):
    if value:
        if not value[0].isalpha():
            raise exceptions.ValidationError("Your name must start with a letter!")
