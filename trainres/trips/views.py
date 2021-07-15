from django.shortcuts import redirect, render
from .models import Booking, Trip
from .filters import BookFilter
from .forms import BookingForm
# Create your views here.


def home(request):
    f = BookFilter(request.GET, queryset=Trip.objects.all())
    
    context = {
        'trips': Trip.objects.all(),
        'filter': f
    }

    return render(request, 'trips/home.html', context)


def book(request, id):
    tripToBook = Trip.objects.get(trip_id=id)

    context = {
        'trip' : tripToBook,
    }

    if request.method == 'POST':
        num = int(request.POST.get('seats',''))
        availableSeats = tripToBook.reserved_seats
        if num > availableSeats:
            context['error'] = 'Too much seats!'
            context['form'] = BookingForm(request.POST)
            return render(request, 'trips/book.html', context)
        obj = Booking(user_id=request.user, trip_id=tripToBook, seats=num)
        obj.save()
        return redirect('trainres-home')
        
    context['form'] = BookingForm()
    return render(request, 'trips/book.html', context)