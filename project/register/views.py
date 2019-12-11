# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from .models import Candidate as Model

from django.shortcuts import render,redirect


from .filter import getDataByFilter
from .form import ModelForm

from django.http import HttpResponseRedirect
from rest_framework.response import Response
import boto


from rest_framework.decorators import api_view
from .authorization import is_admin

@api_view(['POST','GET'])
@is_admin
def download_resume(request):
    try:
        model = Model.objects.get(pk=request.GET.get('id'))
    except:
         return Response({'status':'not_fond'}, status=400)

    conn = boto.connect_s3(None, None)
    bucket = conn.get_bucket('media-staging-ureed')
    s3_file_path = bucket.get_key(model.resume)
    url = s3_file_path.generate_url(expires_in=600)  # expiry time is in seconds

    return Response({'url': url}, status=200)



