
from django import template

register = template.Library()


@register.filter
def get_dict_value(dict, key):
    return dict.get(key)


