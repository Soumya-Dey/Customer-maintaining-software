import django_filters
from django_filters import DateFilter

from .models import *

class OrderFilter(django_filters.FilterSet):
    start_date = DateFilter(field_name = 'date_created', lookup_expr = 'gte') # 'gte' : grater than or equal to
    end_date = DateFilter(field_name = 'date_created', lookup_expr = 'lte') # 'lte' : less than or equal to

    class Meta:
        # filtering for Order data based on all properties
        model = Order
        fields = '__all__'
        exclude = ['customer', 'date_created']
