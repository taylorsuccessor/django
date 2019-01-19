from django.conf.urls import url, include
from rest_framework import routers
from api import ViewSet
from .views import list ,edit,delete


router = routers.DefaultRouter()
router.register(r'api', ViewSet)

# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.
urlpatterns = [
    url(r'^', include(router.urls)),
    url(r'^index/$',list),
    url(r'^edit/(?P<pk>[^/.\?]+)?/?$',edit),
    url(r'^delete/(?P<pk>[^/.\?]+)?/?$',delete)

]