"""Custom Filters for Listing module"""
import django_filters
from .models import Listings


class ListingFilterSet(django_filters.FilterSet):
    """Listing Filters"""
    make = django_filters.CharFilter()

    class Meta:
        model = Listings
        fields = ("make", "year")
        exclude = ['id']
