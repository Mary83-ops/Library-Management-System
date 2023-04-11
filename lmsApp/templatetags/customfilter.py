from django import template

register = template.Library()

@register.filter(name='my_custom_filter')
def my_custom_filter(value):
    # your custom filter code here
    modified_value = value.upper()
    return modified_value

@register.filter(name='replaceBlank')
def replace_blank(value, arg):
    return value.replace(' ', arg)
