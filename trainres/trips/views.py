from django.shortcuts import redirect, render
from .models import Booking, Trip
from .filters import BookFilter
from .forms import BookingForm
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator,EmptyPage
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.views.generic import DeleteView

# Create your views here.


def home(request):
    filteredResult = BookFilter(
        request.GET, queryset=Trip.objects.all()
    )

    page_num = request.GET.get('page', 1)
    p = Paginator(filteredResult.qs, 7)
    
    try:
        page = p.page(page_num)
    except EmptyPage:
        page = p.page(1)

    context = {
        'filter': filteredResult,
        'results' : page
    }

    return render(request, 'trips/home.html', context)

@login_required
def bookings(request):
    userBookings = Booking.objects.filter(user_id=request.user)
    p = Paginator(userBookings, 7)
    page_num = request.GET.get('page', 1)

    try:
        page = p.page(page_num)
    except EmptyPage:
        page = p.page(1)
    
    return render(request, 'trips/bookings.html', {'bookings': page, 'pageOffset': (page.number-1) * 7})

@login_required
def book(request, id):
    tripToBook = Trip.objects.get(trip_id=id)
    payment = request.POST.get('payment_method')

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

        obj = Booking(user_id=request.user, trip_id=tripToBook, seats=num , payment_method= payment)
        obj.save()
        tripToBook.__setattr__('reserved_seats', (availableSeats-num))
        tripToBook.save()
        return redirect('trainres-home')
        
    context['form'] = BookingForm()
    return render(request, 'trips/book.html', context)


class PostDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Booking
    success_url = '/'

    def test_func(self):
        booking = self.get_object()
        if self.request.user == booking.user_id:
            return True
        return False
