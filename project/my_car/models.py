# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.core.validators import MinValueValidator
from user.models import MyUser as User
from django.utils.translation import ugettext_lazy as _

# Create your models here.
def get_upload_path(self, file_name):
    return  "uploads/" + file_name


class Shop(models.Model):
    name=models.CharField(max_length=15)
    owner = models.ForeignKey(User, null=True, blank=True)
    def __str__(self):
        return self.name


class MyCar(models.Model):
    STATUS_AVAILABLE="AE"
    STATUS_NOT_AVAILABLE="NA"

    STATUS_LIST=(
        (STATUS_AVAILABLE, _("available")),
        (STATUS_NOT_AVAILABLE, _("not available"))
    )

    name=models.CharField(max_length=50)
    age=models.IntegerField(default=5)
    owner = models.ForeignKey(User, null=True, blank=True)

    price = models.FloatField(validators=[MinValueValidator(0)], null=True, blank=True)
    number_of_door = models.PositiveIntegerField(verbose_name=_("Number of Doors"), null=True, blank=True)
    temperature = models.IntegerField(null=True, blank=True)

    status = models.CharField(max_length=2, choices=STATUS_LIST, null=True, blank=True)
    shop = models.ForeignKey(Shop, null=True, blank=True)
    show = models.NullBooleanField(default=False,  blank=True)
    img = models.FileField(upload_to=get_upload_path)
    created_at = models.DateTimeField(auto_now_add=True, verbose_name=_("Created at"))
    edited_at = models.DateTimeField(verbose_name=_("Edited At"), null=True, blank=True)
    deleted_at = models.DateField( null=True, blank=True)
    description = models.TextField(verbose_name=_("Description"))

    def status_text(self):
        return dict(self.STATUS_LIST).get(self.status,'')

    def __str__(self):
        return self.name + '( '+str(self.age)+' )'


        # return 'this method in model and used in serializer'



def admin_menu():
    return {'label': 'Car', 'url': '/admin/my_car/mycar', 'name': 'MyCar','icon':'fa fa-car',
            'sub':{
                'MyCar':{'name':'My Car','admin_url':'/admin/my_car/mycar','add_url':'/admin/my_car/mycar/add/'},
                'Shop':{'name':'Shop','admin_url':'/admin/my_car/shop','add_url':'/admin/my_car/shop/add/'},

                 }


            }