from django import template

register = template.Library()



@register.inclusion_tag("admin/filter.html", takes_context=True)
def admin_filter(context,cl, spec):
    return {
        'title': spec.title,
        'choices': list(spec.choices(cl)),
        'spec': spec,
        'filter_container_class':context['filter_container_class'] if 'filter_container_class' in context else  'col-xs-4'
    }
