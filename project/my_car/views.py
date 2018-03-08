# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.forms.models import modelformset_factory
from .admin import MyCarForm
from .models import MyCar

from django.shortcuts import render

from admin import MyCarAdmin


from django.contrib.admin import helpers, widgets
# Create your views here.



def myCarView(request):
    template_name = 'admin/change_form.html'

    myCarFormSet = modelformset_factory(MyCar, form=MyCarForm)
    myCarFormSet.prepopulated_fields={}
    opts={
        'app_label':'my_car',
    }

    adminForm = helpers.AdminForm(
        MyCarForm,
        [(None, {'fields':{'naem'}} )],
        {},
        {},
        model_admin=MyCarAdmin)

    context = dict(
            request,
            title='Add  vvCCXX))NN ',
            adminform=adminForm,
            object_id=3,
            original=MyCar.objects.get(pk=3),
            is_popup=False,
            to_field='',
            media='',
            # inline_admin_formsets=inline_formsets,
            # errors=helpers.AdminErrorList(form, formsets),
            # preserved_filters=self.get_preserved_filters(request),
            opts=opts
        )
    return render(request, template_name, context)