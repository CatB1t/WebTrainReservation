from django import forms
from .models import Trip
import django_filters

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
    widget=forms.TextInput(attrs={'name': 'Departure Time','placeholder':'dd-mm-yyyy', 'class': 'form-control'}) ,
    label="Departure Date")

    dept_time = django_filters.TimeFilter(widget=forms.TextInput(attrs={'placeholder':'hh:mm', 'class': 'form-control'}), label="Departure Time")
    
    class Meta:
        model = Trip
        fields = ['source', 'destination', 'dept_date', 'dept_time']
