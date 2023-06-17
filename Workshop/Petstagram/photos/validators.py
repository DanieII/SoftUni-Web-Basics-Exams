from django.core.exceptions import ValidationError


def image_size_validator(image):
    if image.size > 5242880:
        raise ValidationError("The maximum file size that can be uploaded is 5MB")
