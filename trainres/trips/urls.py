from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='trainres-home'),
    path('bookings/', views.bookings, name='trainres-bookings'),
    path('book/<int:id>', views.book, name='trainres-book')
]
