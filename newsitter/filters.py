import django_filters 
from.models import *

class payment_Filter(django_filters.FilterSet):
    class Meta:
        model = Payment
        fields = ['baby_name']