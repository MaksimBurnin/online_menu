from django import template


register = template.Library()

@register.filter(name='dict_value')
def dict_value(d, key):
    if key in d:
        return d[key]
