from multiprocessing import context
import re
from django.shortcuts import redirect, render
from django.http import HttpResponse
from django.urls import is_valid_path
from .models import Room
from .forms import RoomForm
# Create your views here.

# rooms = [
#     {'id':1, 'name':'lets learn python!'},
#     {'id':2, 'name':'Design with me!'},
#     {'id':3, 'name':'Front developer!'}
# ]

def home(request):
    # return HttpResponse("Home Page")
    # context = {'rooms':rooms}
    # Models.objects.all()  // model_name, model_objects_attribute, method(all, get, filter, exclude)

    rooms = Room.objects.all()
    context = {'rooms':rooms}
    return render(request, 'home.html', context)
    # return render(request, 'home.html', context)

def room(request, pk):
    room = Room.objects.get(id=pk)
    # for i in rooms:
    #     if i in rooms:
    #         room = i
    context = {'room':room}
    return render(request, 'base/room.html', context)

def createRoom(request):
    form = RoomForm()
    if request.method == 'POST':
        form = RoomForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
            
    context = {'form':form}
    return render(request, 'base/room_form.html', context) 

def updateRoom(request, pk):
    room = Room.objects.get(id=pk)
    form = RoomForm(instance=room)

    if request.method == "POST":
        form = RoomForm(request.POST, instance=room)
        if form.is_valid:
            form.save()
            return redirect('home')

    context = {"form":form}
    return render(request, 'base/room_form.html', context)

def deleteRoom(request, pk):
    room = Room.objects.get(id=pk)
    if request.method == "POST":
        room.delete()
        return redirect('home')
    return render(request, 'base/delete_room.html', {'obj': room})