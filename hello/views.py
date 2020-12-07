from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def index(request):
    return HttpResponse("<h1> hello world !</h1>")

def hitansh(request):
    return HttpResponse("<h1>hello Hitansh </h1>")
def greet(request,name):
    #return HttpResponse(f"<h1> Hello {name.upper()} !</h1>")
    return render(request,"hello/greet.html",{
        "name":name
    })