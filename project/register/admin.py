# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from register.models import Candidate



admin.site.register(Candidate)
admin.site.site_header = 'My Administration'



