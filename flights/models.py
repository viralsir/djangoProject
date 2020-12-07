from django.db import models

class Airport(models.Model):
    code=models.CharField(max_length=25)
    city=models.CharField(max_length=55)

    def __str__(self):
        return f"{self.city} ({self.code})"


# Create your models here.
class Flight(models.Model):
    origin=models.ForeignKey(Airport,on_delete=models.CASCADE,related_name="departure")
    destination=models.ForeignKey(Airport,on_delete=models.CASCADE,related_name="arrival")
    duration=models.IntegerField()

    def __str__(self):
        return f"{self.origin}: {self.destination}"

    def is_valid_flight(self):
        return self.origin != self.destination or self.duration>0

class Passenger(models.Model):
    first_name=models.CharField(max_length=50)
    last_name=models.CharField(max_length=30)
    flights=models.ManyToManyField(Flight,blank=True,related_name="passengers")

    def __str__(self):
        return f"{self.first_name} {self.last_name}"

