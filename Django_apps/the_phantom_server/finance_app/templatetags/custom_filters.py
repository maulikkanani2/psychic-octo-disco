from django import template

register = template.Library()

@register.filter(name='subtract_length')
def subtract_length(value, arg):
    return value - arg

@register.filter
def to_str(value):
    """converts int to string"""
    return str(value)