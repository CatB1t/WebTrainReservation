from django.contrib import admin
from .models import Booking, Trip, Train

# Register your models here.
admin.site.register(Trip)
admin.site.register(Train)
admin.site.register(Booking)