from django.shortcuts import render,redirect
from django.forms import forms
from django.forms.fields import CharField,IntegerField

class NewForm(forms.Form):
    task=CharField(label="New Task ")
    priority=IntegerField(label="Priority :",min_value=2,max_value=5)

tasks=["foo","bar","ddd"]
# Create your views here.
def index(request):
    return render(request,"todo/index.html",{
        "tasks":tasks
    })

def add(request):
    form=NewForm()
    if request.method=='POST':
        form=NewForm(request.POST)
        if form.is_valid():
            tasks.append(form.cleaned_data["task"])
        else :
            return render(request,"todo/addtask.html",{
                "form":form
            })
        return redirect("todo:index")

    return render(request,"todo/addtask.html",{
        "form":form
    })