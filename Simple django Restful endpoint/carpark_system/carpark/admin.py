from django.contrib import admin
from .models import Carpark, CarparkType, ParkingSystem

admin.site.register(Carpark)
admin.site.register(CarparkType)
admin.site.register(ParkingSystem)
