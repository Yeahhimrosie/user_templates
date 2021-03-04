from django.shortcuts import render, redirect
from .models import *

def index(request):
    context ={
        "all_users": User.objects.all()
    }
    return render (request, 'index.html', context)

def submit(request):
    if request.method == 'POST':
        print(request.POST)
        user = User.objects.create(name=request.POST['name'], email=request.POST['email'], age=request.POST['age'])
    return redirect('/')
# Create your views here.
