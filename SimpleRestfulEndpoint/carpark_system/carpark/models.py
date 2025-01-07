from django.db import models

class CarparkType(models.Model):
    carparktypeid = models.AutoField(primary_key=True)
    carparktype = models.CharField(max_length=255)

    def __str__(self):
        return self.carparktype

class ParkingSystem(models.Model):
    parksystemid = models.AutoField(primary_key=True)
    typeofparkingsystem = models.CharField(max_length=255)

    def __str__(self):
        return self.typeofparkingsystem

class Carpark(models.Model):
    carparkno = models.CharField(max_length=255, primary_key=True)
    address = models.CharField(max_length=255)
    x_coord = models.CharField(max_length=50)
    y_coord = models.CharField(max_length=50)
    shorttermparking = models.CharField(max_length=50)
    freeparking = models.CharField(max_length=50)
    nightparking = models.CharField(max_length=3)
    carparkingdecks = models.IntegerField()
    gantryheight = models.FloatField()
    carparkbasement = models.CharField(max_length=1)
    carparktype = models.ForeignKey(CarparkType, on_delete=models.CASCADE)
    parksystem = models.ForeignKey(ParkingSystem, on_delete=models.CASCADE)

    def __str__(self):
        return self.carparkno
