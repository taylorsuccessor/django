from django.conf.urls import url, include
from rest_framework import routers
from api import CarViewSet
from .views import myCarView ,edit,delete


router = routers.DefaultRouter()
router.register(r'car', CarViewSet)

# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.
urlpatterns = [
    url(r'^', include(router.urls)),
    url(r'^index/$',myCarView),
    url(r'^create/$',edit),
    url(r'^delete/$',delete)

]