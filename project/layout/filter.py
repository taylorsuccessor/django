from django import template

register = template.Library()

@register.filter(name='article_shorten_body')
def article_shorten_body(bodytext,length):
    return 'filter ddd'