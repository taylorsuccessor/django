import django_filters
from models import MyCar as Model

from django.core.paginator import Paginator



class Filter(django_filters.FilterSet):

    # name = django_filters.CharFilter(name='name', label='Sender Name', method='filter_full_name')



    o = django_filters.OrderingFilter(fields=('id','created_at','status','name'),)



    # def filter_full_name(self, queryset, name, value):
    #     return queryset.select_related('sender').extra(
    #         where=[
    #             "LOWER(auth_user.first_name)||' '||LOWER(auth_user.last_name) LIKE '%%" + str(value).lower() + "%%'"], )


    class Meta:
        model = Model
        # fields=['name','status']
        fields = {
            'id': ['lt', 'gt','exact'],
            'name': ['iexact'],
            'status': ['iexact'],
        }



def getDataByFilter(requestData):

    query_set = Filter(requestData, Model.objects.all()).qs

    per_page = int(requestData.get('per_page',25) )
    paginator = Paginator(query_set, per_page) # Show 25 contacts per page

    page = int(requestData.get('p',1) )

    try:
        contacts = paginator.page(page)
    except:
        contacts = paginator.page(1)





    return {
        'paginator':paginator,
        'results':contacts,
        'total': paginator.count,
        'page':page

    }




from rest_framework.pagination import PageNumberPagination





class StandardPagination(PageNumberPagination):
    page_size = 10
    page_size_query_param = 'page_size'
    max_page_size = 1000
    page_query_param='p'