from django.shortcuts import render

def index(request):
   return render(request, 'bianca/index.html')

def ex001(request):
    return render(request, 'bianca/ex001.html')

