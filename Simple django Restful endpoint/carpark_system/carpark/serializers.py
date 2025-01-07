from rest_framework import serializers
from .models import Carpark, CarparkType

class CarparkSerializer(serializers.ModelSerializer):
    class Meta:
        model = Carpark
        fields = '__all__'

        