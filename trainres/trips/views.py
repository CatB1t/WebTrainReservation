from django.db.models.query import QuerySet
from django.shortcuts import render
from .models import Trip
from .filters import BookFilter
# Create your views here.


def home(request):
    f = BookFilter(request.GET, queryset=Trip.objects.all())

    context = {
        'trips': Trip.objects.all(),
        'filter': f
    }

    return render(request, 'trips/home.html', context)
