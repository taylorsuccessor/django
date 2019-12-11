# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.core.validators import MinValueValidator
from django.utils.translation import ugettext_lazy as _

# Create your models here.
def get_upload_path(self, file_name):
    return  "uploads/" + file_name




class Candidate(models.Model):
    DEPARTMENT_IT="IT"
    DEPARTMENT_HR="HR"
    DEPARTMENT_FINANCE="FINANCE"

    DEPARTMENT_LIST=(
        (DEPARTMENT_IT, _("IT")),
        (DEPARTMENT_HR, _("HR")),
        (DEPARTMENT_FINANCE, _("FINANCE"))
    )


    full_name=models.CharField(max_length=50)
    date_of_birth = models.DateField( null=True, blank=True)
    experience_years=models.IntegerField(default=5)
    department_id = models.CharField(max_length=7, choices=DEPARTMENT_LIST, null=True, blank=True)
    resume = models.FileField(upload_to=get_upload_path)


    def department_text(self):
        return dict(self.DEPARTMENT_LIST).get(self.department_id,'')

    def __str__(self):
        return self.full_name





