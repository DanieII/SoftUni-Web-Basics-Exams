from django import template

register = template.Library()


@register.filter
def get_first_20_chars(value):
    if len(value) > 20:
        value = value[:20] + '...'

    return value
