from django import forms

class Ex001Form(forms.Form):
    texto = forms.CharField( label='texto', widget=forms.Textarea)
    posicao_inicio = forms.IntegerField(label='posição de inicio', required=True)
    posicao_fim = forms.IntegerField(label='posição final', required=True)
