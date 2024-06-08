from django.shortcuts import render,redirect
from .models import *
from .forms import *

def index(request):
    task=Task.objects.all()
    form=Taskform()
    
    if request.method=="POST":
        form=Taskform(request.POST)
        if form.is_valid():
            form.save()  
        return redirect('/')       

    context={'task':task,'form':form}
    return render(request,'index.html',context)

def delete(req,pk):
    task=Task.objects.get(id=pk)
    task.delete()
    return redirect('/')
    

