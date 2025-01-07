import os
import csv
from django.core.management.base import BaseCommand
from carpark.models import Carpark, CarparkType, ParkingSystem


class Command(BaseCommand):
    help = "Load data from HDBCarparkInformation.csv into the database"

    def handle(self, *args, **options):
        # File path to the CSV
        csv_file_path = os.path.join(os.path.dirname(__file__), 'HDBCarparkInformation.csv')

        # Clear existing data
        Carpark.objects.all().delete()
        CarparkType.objects.all().delete()
        ParkingSystem.objects.all().delete()

        # Open the CSV file
        with open(csv_file_path, mode="r", encoding="utf-8") as file:
            reader = csv.DictReader(file)

            for row in reader:
                # Create or get CarparkType
                carpark_type, _ = CarparkType.objects.get_or_create(
                    carparktype=row["car_park_type"].strip()
                )

                # Create or get ParkingSystem
                parking_system, _ = ParkingSystem.objects.get_or_create(
                    typeofparkingsystem=row["type_of_parking_system"].strip()
                )

                # Create Carpark
                Carpark.objects.create(
                    carparkno=row["car_park_no"].strip(),
                    address=row["address"].strip(),
                    x_coord=row["x_coord"].strip(),
                    y_coord=row["y_coord"].strip(),
                    shorttermparking=row["short_term_parking"].strip(),
                    freeparking=row["free_parking"].strip(),
                    nightparking=row["night_parking"].strip(),
                    carparkingdecks=int(row["car_park_decks"].strip()),
                    gantryheight=float(row["gantry_height"].strip()),
                    carparkbasement=row["car_park_basement"].strip(),
                    carparktype=carpark_type,
                    parksystem=parking_system,
                )

        self.stdout.write(self.style.SUCCESS("Data loaded successfully!"))
