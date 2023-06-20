from django import template

register = template.Library()


@register.filter
def filter_characters(value):
    if len(value) > 20:
        return value[:20] + '...'
    return value
