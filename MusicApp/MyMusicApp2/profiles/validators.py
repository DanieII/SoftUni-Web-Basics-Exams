from django.core import exceptions


def validate_username(value):
    if not all([x.isdigit() or x.isalpha() or x == '_' for x in value]) or value.count('_') > 1:
        raise exceptions.ValidationError("Ensure this value contains only letters, numbers, and underscore.")
