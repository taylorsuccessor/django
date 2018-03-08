from django import template

register = template.Library()



@register.inclusion_tag("admin/filter.html", takes_context=True)
def admin_filter(context,cl, spec):
    return {
        'title': spec.title,
        'choices': list(spec.choices(cl)),
        'spec': spec,
        'filter_container_class':context['filter_container_class'] if context['filter_container_class'] else  'col-xs-4'
    }
