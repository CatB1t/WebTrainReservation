from django.contrib.auth.forms import AuthenticationForm
from django.urls import path
from django.contrib.auth import views as auth_views
from . import views
from . import forms

urlpatterns = [
    path('login/', auth_views.LoginView.as_view(template_name='users/login.html', authentication_form=forms.UserLoginForm), name='users-login'),
    path('register/', views.register, name='users-register'),
    path('logout/', views.logout_view, name='users-logout'),
    path('profile/', views.profile, name='users-profile')
]
