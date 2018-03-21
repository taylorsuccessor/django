from serializer import CarSerializer
from models import MyCar

from rest_framework import viewsets
from filter import CarFilter

from rest_framework import filters
from rest_framework.response import Response

from rest_framework.pagination import PageNumberPagination





class StandardPagination(PageNumberPagination):
    page_size = 10
    page_size_query_param = 'page_size'
    max_page_size = 1000
    page_query_param='page'

class CarViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = MyCar.objects.all().order_by('id')
    serializer_class = CarSerializer
    pagination_class = StandardPagination





    def get_queryset(self):
        query_set = self.queryset

        if self.request.GET.get('name',False):
              query_set = query_set.filter(name=self.request.GET.get('name'))

        sort='' if self.request.GET.get('sort',False) !='desc' else '-'
        order_by=self.request.GET.get('order_by') if self.request.GET.get('order_by',False) else 'id'
        query_set = query_set.order_by(sort + order_by)




        return query_set


    def list(self, request, *args, **kwargs):
        queryset = self.filter_queryset(self.get_queryset())

        page = self.paginate_queryset(queryset)
        if page is not None:
            serializer = self.get_serializer(page, many=True)
            return self.get_paginated_response(serializer.data)

        serializer = self.get_serializer(queryset, many=True)

        return Response(serializer.data )