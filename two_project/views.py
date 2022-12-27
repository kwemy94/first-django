from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def index(request):
    donnees ={'ras': 'juste des test de similtude django / laravel'}
    return render(request, 'index.html', context=donnees)

def store(request):
    return HttpResponse("<em> Route with url </em>")
