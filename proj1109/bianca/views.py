from django.shortcuts import render
from .forms import Ex001Form
import ast

def index(request):
   return render(request, 'bianca/index.html')

def qualquer(texto, valor):
    result = texto * valor
    return result

def qualquer2(texto):
    lista = ast.literal_eval(texto)
    print("LISTA")
    print(lista)
    return lista[-2], lista[-1]

def qualquer3(texto, posicao):
    lista = ast.literal_eval(texto)
    return lista[(posicao - 1)]

def qualquer4(texto, posicao_inicio, posicao_fim):
    lista = ast.literal_eval(texto)
    return lista[(posicao_inicio -1):(posicao_fim -1)]

def ex001(request):  
    ip_address = request.META.get('REMOTE_ADDR')
    passo = ''
    if request.method == 'POST':
        metodo = "*POST*"
        form = Ex001Form(request.POST)
        if form.is_valid():
            texto = form.cleaned_data['texto']
            posicao_inicio = int(form.cleaned_data['posicao_inicio'])
            posicao_fim = int(form.cleaned_data['posicao_fim'])
            passo = qualquer4(texto, posicao_inicio, posicao_fim)
    else:
        metodo = "*GET*"      
        initial_data = {
            'texto': 'texto padrão',
            'posicao_inicio': 1,
            'posicao_fim': 2,
            'passo': 'teste',
        }
        form = Ex001Form(initial=initial_data)


    context = { 
        'titulo' : 'historia do passos',
        'passo' : passo,
        'metodo' : metodo,
        'ip_address' : ip_address,
        'form' : form,
    }
    
    return render(request, 'bianca/ex001.html', context)

