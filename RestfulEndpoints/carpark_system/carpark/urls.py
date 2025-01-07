from django.urls import path, register_converter
from . import views
from .views import (
    CarparkByGantryHeight,
    NoParking,
    AddCarpark,
    UpdateCarpark,
    DeleteCarpark,
    CarparksWithNightParking,
)

from .converters import FloatConverter

register_converter(FloatConverter, 'float')

urlpatterns = [
    path("", views.home, name="home"),
    path('carparks/gantry_height/<float:height>/', CarparkByGantryHeight.as_view(), name='carpark_by_height'),
    path('carparks/no_parking/', NoParking.as_view(), name='no_parking'),
    path('carparks/add/', AddCarpark.as_view(), name='add_carpark'),
    path('carparks/update/<str:carparkno>/', UpdateCarpark.as_view(), name='update_carpark'),
    path('carparks/delete/<str:carparkno>/', DeleteCarpark.as_view(), name='delete_carpark'),
    path('carparks/night_parking/', CarparksWithNightParking.as_view(), name='night_parking'),
]

