import django_filters
from models import MyCar




class CarFilter(django_filters.FilterSet):

    # name = django_filters.CharFilter(name='name', label='Sender Name', method='filter_full_name')



    o = django_filters.OrderingFilter(
        # tuple-mapping retains order
        fields=(
            'created_at',
            'status',
            'name'
        ),
    )


    # def filter_full_name(self, queryset, name, value):
    #     return queryset.select_related('sender').extra(
    #         where=[
    #             "LOWER(auth_user.first_name)||' '||LOWER(auth_user.last_name) LIKE '%%" + str(value).lower() + "%%'"], )


    class Meta:
        model = MyCar
        # fields=['name','status']
        fields = {
            'id': ['lt', 'gt'],
            'name': ['iexact'],
            'status': ['iexact'],
        }


