from django.core.exceptions import ValidationError


def name_validator(value):
    if not all(x.isalpha() for x in value):
        raise ValidationError('Plant name should contain only letters!')
