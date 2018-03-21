import django_filters
from models import MyCar

class CarFilter(django_filters.FilterSet):
    class Meta:
        model = MyCar
        fields = ['name', 'price', 'status']







class MessageFilter(django_filters.FilterSet):

    full_name = django_filters.CharFilter(name='name', label='Sender Name', method='filter_full_name')



    o = django_filters.OrderingFilter(
        # tuple-mapping retains order
        fields=(
            'create_date',
        ),
    )


    def filter_full_name(self, queryset, name, value):
        return queryset.select_related('sender').extra(
            where=[
                "LOWER(auth_user.first_name)||' '||LOWER(auth_user.last_name) LIKE '%%" + str(value).lower() + "%%'"], )



    class Meta:
        model = MyCar
        fields = {
            'id': ['lt', 'gt'],
        }

