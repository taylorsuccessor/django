from rest_framework.compat import is_authenticated
from django.core.urlresolvers import resolve

class BasePermission(object):

    def has_permission(self, request, view):
        return True

    def has_object_permission(self, request, view, obj):
        return True



class IsAuthenticated(BasePermission):

    def has_permission(self, request, view):
        return request.user and is_authenticated(request.user)



class IsAuthorized(BasePermission):

    def has_permission(self, request, view=None):
        current_url = resolve(request.path_info).url_name
        print current_url
        return True
        return request.user and is_authenticated(request.user)






class AllowAny(BasePermission):

    def has_permission(self, request, view):
        return True