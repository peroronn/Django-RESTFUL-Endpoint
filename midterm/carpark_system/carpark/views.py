from rest_framework.views import APIView
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .models import Carpark
from .serializers import CarparkSerializer
from django.shortcuts import render


def home(request):
    return render(request, "index.html")

# 1. Retrieve car parks with gantry height greater than specified value
class CarparkByGantryHeight(APIView):
    def get(self, request, height):
        if height < 0:
            return Response(
                {"error": "Gantry height must be a positive number."},
                status=status.HTTP_400_BAD_REQUEST,
            )
        carparks = Carpark.objects.filter(gantryheight__gt=height)
        serializer = CarparkSerializer(carparks, many=True)
        return Response(serializer.data)

# 2. Retrieve car parks with no parking
class NoParking(APIView):
    def get(self, request):
        carparks = Carpark.objects.filter(freeparking__icontains="NO")
        serializer = CarparkSerializer(carparks, many=True)
        return Response(serializer.data)

# 3. Add a new car park entry
class AddCarpark(APIView):
    def post(self, request):
        print("Request data:", request.data)  # Debugging
        serializer = CarparkSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        print("Errors:", serializer.errors)  # Debugging
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# 4. Update car park details by carparkno
class UpdateCarpark(APIView):
    def put(self, request, carparkno):
        try:
            carpark = Carpark.objects.get(carparkno=carparkno)
        except Carpark.DoesNotExist:
            return Response({'error': 'Carpark not found'}, status=status.HTTP_404_NOT_FOUND)

        serializer = CarparkSerializer(carpark, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# 5. Delete a car park by carparkno
class DeleteCarpark(APIView):
    def delete(self, request, carparkno):
        try:
            carpark = Carpark.objects.get(carparkno=carparkno)
        except Carpark.DoesNotExist:
            return Response({'error': 'Carpark not found'}, status=status.HTTP_404_NOT_FOUND)

        carpark.delete()
        return Response({'message': 'Carpark deleted successfully'}, status=status.HTTP_204_NO_CONTENT)


# 6. Retrieve car parks with night parking
class CarparksWithNightParking(APIView):
    def get(self, request):
        carparks = Carpark.objects.filter(nightparking="YES")
        serializer = CarparkSerializer(carparks, many=True)
        return Response(serializer.data)
