from django.shortcuts import render,redirect
from django.http import HttpResponse
from .models import *
from .forms import *

def index(request):
    myapps=Task.objects.all()
    form=TaskForm()
    if request.method=="POST":
        form=TaskForm(request.POST)
        if form.is_valid():
            form.save()
        return redirect('/')

    context={
        'myapps':myapps,
        'form':form
    }
    return  render(request,'list.html',context)

def updateTask(request,pk):
    task=Task.objects.get(id=pk)

    form=TaskForm(instance=task)
    if request.method=="POST":
        form=TaskForm(request.POST,instance=task)
        if form.is_valid():
            form.save()
            return redirect('/')

    context={
        'form':form
    }


    return render(request,'update_task.html',context)

def deleteTask(request,pk):
    item=Task.objects.get(id=pk)
    if request.method=="POST":
        item.delete()
        return redirect('/')

    context={
        'item':item
    }

    return render(request,'delete.html',context)
