import re

from django.conf import settings
from django.http import HttpResponsePermanentRedirect
from django.utils.deprecation import MiddlewareMixin
from .authorization import IsAuthorized


class authorization(MiddlewareMixin):

    def process_request(self, request):
        isAuthorized=IsAuthorized();
        if  not isAuthorized.has_permission(request):
            return HttpResponsePermanentRedirect(
                '/admin/login'
            )

    def process_response(self, request, response):
        return response
