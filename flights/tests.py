from django.test import TestCase,Client
from .models import Airport,Flight
# Create your tests here.
class FlightTest(TestCase):

    def setUp(self) :

        # create airport objects
        a1=Airport.objects.create(code='ahm',city='Ahmedabad')
        a2=Airport.objects.create(code='bom',city='Bombay')

        # create flights
        f1=Flight.objects.create(origin=a1,destination=a2,duration=200)
        f2=Flight.objects.create(origin=a1,destination=a1,duration=200)
        f3=Flight.objects.create(origin=a1,destination=a2,duration=-100)


    def test_departure_count(self):
        a=Airport.objects.get(code="ahm")
        self.assertEqual(a.departure.count(),3)

    def test_arrival_count(self):
        a=Airport.objects.get(code='ahm')
        self.assertEqual(a.arrival.count(),1)

    def test_valid_flight(self):
        a1=Airport.objects.get(code='ahm')
        a2=Airport.objects.get(code='bom')
        f=Flight.objects.get(origin=a1,destination=a2,duration=200)
        self.assertTrue(f.is_valid_flight())

    def test_invalid_flight_destions(self):
        a1=Airport.objects.get(code='ahm')
        a2=Airport.objects.get(code='bom')
        f=Flight.objects.get(origin=a1,destination=a1,duration=200)
        self.assertFalse(f.is_valid_flight())

    def test_invalid_flight_durations(self):
        a1 = Airport.objects.get(code='ahm')
        a2 = Airport.objects.get(code='bom')
        f = Flight.objects.get(origin=a1, destination=a2, duration=-100)
        self.assertFalse(f.is_valid_flight())

    def test_index(self):
        c=Client()
        response=c.get("/flights/")
        self.assertEqual(response.status_code,200)
        self.assertEqual(response.context["flights"].count(),3)

    # def test_flight_detail_page(self):
    #     c=Client();
    #     a1=Airport.objects.get(code='ahm')
    #     a2=Airport.objects.get(code='bom')
    #     fl=Flight.objects.get(origin=a1,destination=a2,duration=200)
    #
    #     response=c.get(f"/flights/{fl.id}")
    #     self.assertEqual(response.status_code,200)






