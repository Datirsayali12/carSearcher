import django_filters
from .models import *
class ListingFilter(django_filters.FilterSet):
    #barand = django_filters.CharFilter(lookup_expr='iexact')

    class Meta:
        model = Listing
        fields = {'brand':{'exact'},'mileage':{'lt'},'model':{'icontains'}}