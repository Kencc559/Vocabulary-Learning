#file: users/views.py

from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def login(request):
    if request.method == 'GET':
        print("GET")
        return render(request, "login.html")
    elif request.method == "POST":
        print("POST")
        username = request.POST.get("username",'')
        password = request.POST.get("password",'')
        return HttpResponse(username+'<br>'+password)

def registor(request):
    return render(request, "register.html")

def logout(request):
    pass
