from django import template

register = template.Library()

@register.filter
def mul(value, exponent):
    return value * exponent

@register.filter
def percentIncrease(value, percent):
    newValue = value * (1 + percent / 100)
    return round(newValue)