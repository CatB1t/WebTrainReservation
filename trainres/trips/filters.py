import django_filters
from django import forms
from .models import Trip

class BookFilter(django_filters.FilterSet):
    source_choices = [(i['source'], i['source']) for i in Trip.objects.values('source').distinct()]
    source = django_filters.ChoiceFilter(
        choices=source_choices,
        label="From",
        widget=forms.Select(attrs={'class':'form-control mb-2"'}))

    destination_choices = [(i['destination'], i['destination']) for i in Trip.objects.values('destination').distinct()]
    destination = django_filters.ChoiceFilter(choices=destination_choices,
         label="To",
        widget=forms.Select(attrs={'class':'form-control'}))

    dept_date = django_filters.DateFilter(input_formats=['%d-%m-%Y'], 
    widget=forms.TextInput(attrs={'placeholder':'dd-mm-yyyy', 'class': 'form-control'}) ,
    label="Date")

    dept_time = django_filters.TimeFilter(widget=forms.TextInput(attrs={'placeholder':'hh:mm', 'class': 'form-control'}), label="Time")

    available_seats = django_filters.NumberFilter(
        method='minSeat', widget=forms.NumberInput(attrs={'class': 'form-control', 'min': '1'}),
        label="Minimum Slots")

    def minSeat(self,qs,name,value):
        return qs.filter(available_seats__gte=value)
    
    class Meta:
        model = Trip
        fields = ['source', 'destination', 'dept_date',
                  'dept_time', 'available_seats']
