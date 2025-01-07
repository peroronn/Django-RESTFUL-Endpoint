from rest_framework.test import APITestCase
from rest_framework import status
from .models import Carpark, CarparkType, ParkingSystem


class CarparkTests(APITestCase):
    
    @classmethod
    def setUpTestData(cls):
        # Create a CarparkType instance for ForeignKey relation
        cls.carpark_type = CarparkType.objects.create(carparktype="Testing Carpark Type")
        
        # Create a ParkingSystem instance for ForeignKey relation
        cls.parking_system = ParkingSystem.objects.create(typeofparkingsystem="Testing Parking System")
        
        # Create a sample Carpark entry
        cls.carpark = Carpark.objects.create(
            carparkno="CP001",
            carparktype=cls.carpark_type,
            address="123 Test Street",
            x_coord=1.12345,
            y_coord=103.12345,
            shorttermparking="YES",
            freeparking="YES",
            nightparking="YES",
            carparkingdecks=2,
            gantryheight=2.5,
            carparkbasement="Y",
            parksystem=cls.parking_system
        )

    # Test 3: Add a new car park entry
    def test_add_carpark(self):
        payload = {
            "carparkno": "CP002",
            "carparktype": self.carpark_type.carparktypeid,  # Use carparktypeid instead of id
            "address": "456 Test Avenue",
            "x_coord": 2.34567,
            "y_coord": 104.56789,
            "shorttermparking": "NO",
            "freeparking": "NO",
            "nightparking": "NO",
            "carparkingdecks": 1,
            "gantryheight": 2.0,
            "carparkbasement": "N",
            "parksystem": self.parking_system.parksystemid
        }
        response = self.client.post('/api/carparks/add/', data=payload)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(response.data["carparkno"], "CP002")

    # Test 4: Update an existing car park entry
    def test_update_carpark(self):
        payload = {
            "carparkno": "CP001",
            "carparktype": self.carpark_type.carparktypeid,  # Use carparktypeid instead of id
            "address": "Updated Address",
            "x_coord": 3.33333,
            "y_coord": 105.55555,
            "shorttermparking": "NO",
            "freeparking": "YES",
            "nightparking": "NO",
            "carparkingdecks": 3,
            "gantryheight": 3.0,
            "carparkbasement": "Y",
            "parksystem": self.parking_system.parksystemid
        }
        response = self.client.put(f'/api/carparks/update/{self.carpark.carparkno}/', data=payload)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data["address"], "Updated Address")


    # Test 5: Delete a car park entry
    def test_delete_carpark(self):
        # Check if carpark exists before deletion
        carpark_before_deletion = Carpark.objects.count()
        response = self.client.delete(f'/api/carparks/delete/{self.carpark.carparkno}/')
        # Assert deletion success
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        # Assert one carpark is deleted
        self.assertEqual(Carpark.objects.count(), carpark_before_deletion - 1)


    # Test 6: Get car parks with night parking
    def test_get_carparks_with_night_parking(self):
        response = self.client.get('/api/carparks/night_parking/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertGreater(len(response.data), 0)
        # Check if all carparks returned have night parking enabled
        for carpark in response.data:
            self.assertEqual(carpark['nightparking'], 'YES')

