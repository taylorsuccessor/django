# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from .models import MyCar as Model

from django.shortcuts import render,redirect


from .filter import getDataByFilter
from .form import ModelForm


def myCarView(request):

    context=getDataByFilter(request.GET)
    context.update( {'request':request})
    return render(request, 'index.html', context)


def edit(request):
    id=request.GET.get('id',False)


    if id and request.method!='POST':
        model=Model.objects.get(pk=id)
        modelForm=ModelForm(instance=model)

    elif request.method=='POST':
        if id:
            model=Model.objects.get(pk=id)
            modelForm = ModelForm(request.POST, instance=model)
        else:
            modelForm=ModelForm(request.POST,request.FILES)

        if modelForm.is_valid():
                modelForm.save()
                return redirect('/car/index/')
    else:
        modelForm = ModelForm()


    return render(request,'edit.html',locals())


def delete(request):
    Model.objects.get(pk=request.GET.get('id')).delete()
    return redirect('/car/index/')