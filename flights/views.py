from django.shortcuts import render
from .models import Flight,Passenger
from django.http import HttpResponseRedirect
from django.urls import reverse

# Create your views here.
def index(request):
    flights=Flight.objects.all()
    return render(request,"flights/index.html",{
        "flights":flights
    })

def flight_details(request,flight_id):
    flight=Flight.objects.get(id=flight_id)
    pasengers=flight.passengers.all()
    non_passengers=Passenger.objects.exclude(flights=flight).all()
    return render(request,"flights/flight_details.html",{
        "flight":flight,
        "passengers":pasengers,
        "non_passengers":non_passengers
    })

def book(request,flight_id):
    if request.method == 'POST':
        flight=Flight.objects.get(pk=flight_id)
        passenger=Passenger.objects.get(pk=int(request.POST["passenger"]))
        passenger.flights.add(flight)
        print("passenger is added")
        return HttpResponseRedirect(reverse("details",args=(flight_id,)))

def showcounter(request):
    return render(request,"flights/counter.html")