from django.shortcuts import render
from .models import Trip
# Create your views here.


def home(request):
    context = {
        'trips': Trip.objects.all()
    }
    return render(request, 'trips/home.html', context)
