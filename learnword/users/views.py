#file: users/views.py

from django.shortcuts import render

# Create your views here.

def login_view(request):
    if request.method == 'GET':
        return render(request, "login.html")

def registor_view(request):
    return render(request, "register.html")