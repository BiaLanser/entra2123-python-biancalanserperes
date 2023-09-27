from django.shortcuts import render
from .forms import Ex001Form, Ex003Form
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

def qualquer5(valor):
    return valor.upper()

def ex001(request):  
    ip_address = request.META.get('REMOTE_ADDR')
    passo = ''
    if request.method == 'POST':
        metodo = "*POST*"
        form = Ex001Form(request.POST)
        if form.is_valid():
            texto = form.cleaned_data['texto']
            # texto = qualquer5(texto)
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

def ex003(request):
    ip_address = request.META.get('REMOTE_ADDR')
    if request.method == 'POST':
        form = Ex003Form(request.POST)
        if form.is_valid():
            resposta = form.cleaned_data['resposta']
            if resposta == 'A':  # 'A' significa Paris, que é a resposta correta
                msg = "Parabéns, você acertou!"
            else:
                msg = "Ops, tente novamente."
    else:
        form = Ex003Form(initial={'pergunta': 'Qual é a capital da França?'})
        msg = ""

    context = { 
        'titulo' : 'historia do passos',
        'resposta': 'teste',
        'ip_address' : ip_address,
        'form' : form,
    }

    return render(request, 'bianca/ex003.html', context)


def ex004(request):
    meu_dicionario= {
	    '1' : { 
		    'Pergunta' : 'Qual a capital da França?',
			'A' : 'Blumenau',
			'B' : 'Brusque',
		    'C' : 'Floripa',
			'D' : 'Paris',
			'Resposta' : 'D'
		} ,
        '2': {
            'Pergunta': 'Qual é o maior rio do mundo?',
            'A': 'Rio Nilo',
            'B': 'Rio Amazonas',
            'C': 'Rio Yangtzé',
            'D': 'Rio Mississippi',
            'Resposta': 'B'
        },
        '3': {
            'Pergunta': 'Quem escreveu a peça "Hamlet"?',
            'A': 'William Wordsworth',
            'B': 'William Shakespeare',
            'C': 'Charles Dickens',
            'D': 'George Orwell',
            'Resposta': 'B'
        },
        '4': {
            'Pergunta': 'Qual é o maior deserto do mundo?',
            'A': 'Deserto do Atacama',
            'B': 'Deserto de Gobi',
            'C': 'Deserto do Saara',
            'D': 'Deserto do Kalahari',
            'Resposta': 'C'
        },
        '5': {
            'Pergunta': 'Quem foi o primeiro homem a pisar na Lua?',
            'A': 'Neil Armstrong',
            'B': 'Buzz Aldrin',
            'C': 'Yuri Gagarin',
            'D': 'Alan Shepard',
            'Resposta': 'A'
        }

    }
    print(meu_dicionario)
    print("X"*40)
    for chave, pergunta in sorted(meu_dicionario.items()):
        print(f"Pergunta {chave}: {pergunta['Pergunta']}")
        print(f"A) {pergunta['A']}")
        print(f"B) {pergunta['B']}")
        print(f"C) {pergunta['C']}")
        print(f"D) {pergunta['D']}")
        print('-' * 40)
    
    context = { 
        'meu_dicionario': meu_dicionario,
        'teste': len(meu_dicionario)
    }

    return render(request, 'bianca/ex004.html', context)

    
    
    

