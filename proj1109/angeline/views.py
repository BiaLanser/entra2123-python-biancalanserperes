from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.# Create your views here.

def qualquer(frutas):
   return frutas * 2

def index(request):
   print(qualquer(25))
   return HttpResponse ('hello world')

def ex002(request):
    context = {
        'minha_string': 'Olá, Mundo!',
        'meu_inteiro': 123,
        'meu_booleano': True
    }
    return render(request, 'angeline/ex002.html', context)
