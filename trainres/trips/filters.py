from .models import Trip
import django_filters


class BookFilter(django_filters.FilterSet):
    class Meta:
        model = Trip
        fields = ['source', 'destination']

