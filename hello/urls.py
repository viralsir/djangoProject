from django.urls import path
from . import views

urlpatterns=[
    path("",views.index,name="home"),
    path("<str:name>",views.greet,name="greet"),
    path("hitansh", views.hitansh, name="hitansh"),

]