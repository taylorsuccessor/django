from serializer import Serializer
from models import MyCar as Model

from rest_framework import viewsets
from filter import Filter,getDataByFilter

from rest_framework import filters
from rest_framework.response import Response
from .filter import StandardPagination



from .filter import Filter



class ViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = Model.objects.all().order_by('id')
    serializer_class = Serializer
    pagination_class = StandardPagination





    def get_queryset(self):

        query_set = Filter(self.request.GET, self.queryset).qs



        return query_set


    def list(self, request, *args, **kwargs):
        queryset =  self.get_queryset()

        page = self.paginate_queryset(queryset)
        if page is not None:
            serializer = self.get_serializer(page, many=True)
            return self.get_paginated_response(serializer.data)

        serializer = self.get_serializer(queryset, many=True)

        return Response(serializer.data )