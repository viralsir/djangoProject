from django.urls import path
from .views import index,flight_details,book,showcounter
urlpatterns=[
    path("",index,name="index"),
    path("<int:flight_id>/",flight_details,name="details"),
    path("book/<int:flight_id>/",book,name="book"),
    path("counter",showcounter,name="counter")
]