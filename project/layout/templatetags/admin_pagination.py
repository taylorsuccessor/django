
from django.utils.html import format_html
from django.utils.safestring import mark_safe
from django.contrib.admin.views.main import (
    ALL_VAR, ORDER_VAR, PAGE_VAR, SEARCH_VAR,
)

from django import forms

from django import template

register = template.Library()

DOT='.'


class PaginationForm(forms.Form):
    per_page = forms.IntegerField(label='Per-page',widget=forms.TextInput(attrs={'class':'form-control input-sm'}))
    p=forms.IntegerField(label='Page',widget=forms.TextInput(attrs={'class':' form-control input-sm'}))

@register.simple_tag
def admin_paginator_number(cl, i):
    """
    Generates an individual page index link in a paginated list.
    """
    if i == DOT:
        return format_html('<li ><span>...</span></li> ')
    elif i == cl.page_num:
        return format_html('<li class="active"><span>{}</span></li> ', i + 1)
    else:
        return format_html(' <li><a href="{}" {}>{}</a></li>',
                           cl.get_query_string({PAGE_VAR: i}),
                           mark_safe(' class="end"' if i == cl.paginator.num_pages - 1 else ''),
                           i + 1)


@register.inclusion_tag("admin/partial/pagination.html", takes_context=True)
def admin_pagination(context, cl):
    """
    Generates the series of links to the pages in a paginated list.
    """
    paginator, page_num = cl.paginator, cl.page_num

    pagination_required = (not cl.show_all or not cl.can_show_all) and cl.multi_page
    if not pagination_required:
        page_range = []
    else:
        ON_EACH_SIDE = 3
        ON_ENDS = 2

        # If there are 10 or fewer pages, display links to every page.
        # Otherwise, do some fancy
        if paginator.num_pages <= 10:
            page_range = range(paginator.num_pages)
        else:
            # Insert "smart" pagination links, so that there are always ON_ENDS
            # links at either end of the list of pages, and there are always
            # ON_EACH_SIDE links at either end of the "current page" link.
            page_range = []
            if page_num > (ON_EACH_SIDE + ON_ENDS):
                page_range.extend(range(0, ON_ENDS))
                page_range.append(DOT)
                page_range.extend(range(page_num - ON_EACH_SIDE, page_num + 1))
            else:
                page_range.extend(range(0, page_num + 1))
            if page_num < (paginator.num_pages - ON_EACH_SIDE - ON_ENDS - 1):
                page_range.extend(range(page_num + 1, page_num + ON_EACH_SIDE + 1))
                page_range.append(DOT)
                page_range.extend(range(paginator.num_pages - ON_ENDS, paginator.num_pages))
            else:
                page_range.extend(range(page_num + 1, paginator.num_pages))

    need_show_all_link = cl.can_show_all and not cl.show_all and cl.multi_page


    paginationForm=PaginationForm(context['request'].GET)


    return {
        'cl': cl,
        'pagination_required': pagination_required,
        'show_all_url': need_show_all_link and cl.get_query_string({ALL_VAR: ''}),
        'page_range': page_range,
        'ALL_VAR': ALL_VAR,
        '1': 1,
        'paginationForm':paginationForm,
    }




