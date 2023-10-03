from django import forms

class Ex001Form(forms.Form):
    texto = forms.CharField( label='texto', widget=forms.Textarea)
    posicao_inicio = forms.IntegerField(label='posição de inicio', required=True)
    posicao_fim = forms.IntegerField(label='posição final', required=True)

class Ex003Form(forms.Form):
    PERGUNTA_CHOICES = [
        ('A', 'Paris'),
        ('B', 'Brasília'),
        ('C', 'Estocolmo'),
        ('D', 'Nova York'),
    ]

    pergunta = forms.CharField(disabled=True, label="Pergunta")
    resposta = forms.ChoiceField(choices=PERGUNTA_CHOICES, label="Resposta")

# class Ex006Form(form):
# 	id =
#     nome =
#     qtd =
