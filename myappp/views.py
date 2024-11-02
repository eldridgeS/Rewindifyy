from django.shortcuts import render
from django.http import HttpResponse


def index(request):
    return render(request, 'myappp/home.html')
def base(request):
    return render(request, 'myappp/base.html')
def login(request):
    return render(request, 'myappp/login.html')
def signup(request):
    return render(request, 'myappp/signup.html')