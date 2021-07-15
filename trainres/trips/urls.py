from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='trainres-home'),
    path('book/<int:id>', views.book, name='trainres-book')
]
