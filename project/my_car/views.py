# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.forms.models import modelformset_factory
from .admin import MyCarForm
from .models import MyCar

from django.shortcuts import render

from admin import MyCarAdmin


from django.contrib.admin import helpers, widgets
# Create your views here.

from django.core.paginator import Paginator


import django_filters

class MyCarFilter(django_filters.FilterSet):
    class Meta:
        model = MyCar
        fields = ['name', 'price', 'status']



def myCarView(request):

    resultsFilter=MyCarFilter(request.GET,MyCar.objects.all())

    per_page = int(request.GET.get('per_page',25) )
    paginator = Paginator(resultsFilter.qs, per_page) # Show 25 contacts per page

    page = int(request.GET.get('p',1) )
    contacts = paginator.page(page)




    context={
        'paginator':paginator,
        'results':contacts,
        'total': paginator.count,
        'page':page

    }
    return render(request, 'index.html', context)