from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='trainres-home'),
    path('bookings/', views.bookings, name='trainres-bookings'),
    path('book/<int:id>', views.book, name='trainres-book'),
    path('bookings/<int:id>' , views.booking_details, name='booking-details'),
    path('bookings/<int:id>/delete' , views.booking_delete, name='booking-delete'),
    path('bookings/<int:id>/confirmation' , views.delete, name='delete')
]
