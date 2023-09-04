"""História: Como um programador iniciante em Python, preciso de um programa que possa gerar uma senha aleatória
para mim com comprimento e complexidade especificados. O programa deve me permitir escolher o comprimento da 
senha e os tipos de caracteres a incluir (letras minúsculas, letras maiúsculas, números e caracteres especiais).
A senha gerada deve ser exibida na tela.

Requisitos:

- O programa deve ser escrito em Python e não deve exigir nenhuma biblioteca externa.
- O usuário deve ser capaz de especificar o comprimento da senha.
- O usuário deve ser capaz de escolher quais tipos de caracteres incluir na senha (letras minúsculas, letras maiúsculas, números e caracteres especiais).
- A senha deve ser gerada aleatoriamente e exibida na tela.
- O programa deve ser fácil de usar e entender para programadores iniciantes em Python."""

import random
import string

def gerar_senha(comprimento, usar_letras_min, usar_letras_mai, usar_numeros, usar_especiais):
    caracteres = ''
    
    if usar_letras_min:
        caracteres += string.ascii_lowercase
    if usar_letras_mai:
        caracteres += string.ascii_uppercase
    if usar_numeros:
        caracteres += string.digits
    if usar_especiais:
        caracteres += string.punctuation
    
    senha = ''.join(random.choice(caracteres) for _ in range(comprimento))
    return senha

def main():
    print("Gerador de Senhas Aleatórias")
    comprimento = int(input("Comprimento da senha: "))
    
    usar_letras_min = input("Incluir letras minúsculas? (S/N): ").strip().lower() == 's'
    usar_letras_mai = input("Incluir letras maiúsculas? (S/N): ").strip().lower() == 's'
    usar_numeros = input("Incluir números? (S/N): ").strip().lower() == 's'
    usar_especiais = input("Incluir caracteres especiais? (S/N): ").strip().lower() == 's'
    
    senha = gerar_senha(comprimento, usar_letras_min, usar_letras_mai, usar_numeros, usar_especiais)
    
    print("\nSenha gerada:", senha)

if __name__ == "__main__":
    main()
