from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(request):    
    return render(request, 'index.html')

def hello_world(request):
    return HttpResponse("Olá mundo")

def bia(request):
    return HttpResponse("Bia Linda")