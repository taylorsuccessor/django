from django.conf.urls import url, include
from rest_framework import routers
from .api import ViewSet
from .views import download_resume


router = routers.DefaultRouter()
router.register(r'register', ViewSet)

# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.
urlpatterns = [
    url(r'^', include(router.urls)),
    url(r'^download_resume/$',download_resume),
    # url(r'^edit/(?P<pk>[^/.\?]+)?/?$',edit),
    # url(r'^delete/(?P<pk>[^/.\?]+)?/?$',delete)

]