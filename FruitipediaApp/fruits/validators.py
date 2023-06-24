from django.core import validators


def name_validator(value):
    if not all([x.isalpha() for x in value]):
        raise validators.ValidationError("Fruit name should contain only letters!")
