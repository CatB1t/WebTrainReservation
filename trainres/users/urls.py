from django.urls import path
from . import views

urlpatterns = [
    path('register/', views.register, name='users-register'),
    path('logout/', views.logout_view, name='users-logout')
]
