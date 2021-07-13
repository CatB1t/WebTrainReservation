import django
from .models import Trip
import django_filters

class BookFilter(django_filters.FilterSet):
    source_choices = [(i['source'], i['source']) for i in Trip.objects.values('source').distinct()]
    source = django_filters.ChoiceFilter(choices=source_choices)

    destination_choices = [(i['destination'], i['destination']) for i in Trip.objects.values('destination').distinct()]
    destination = django_filters.ChoiceFilter(choices=destination_choices)

    dept_date = django_filters.DateFilter(input_formats=
        ['%Y-%m-%d',
        '%m/%d/%Y',
        '%m/%d/%y'])

    dept_time = django_filters.TimeFilter()
    
    class Meta:
        model = Trip
        fields = ['source', 'destination', 'dept_date', 'dept_time']
