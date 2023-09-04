"""Preciso de um programa onde eu informe um frase e o programa divide todos os caracteres da minha frase e 
imprima um por um na tela, letra por letra, saltando linha entre as letras impressas, e de uma pausa de 1 
segundo entre cada impressao."""

import minha_biblioteca

def main():
    frase = input("Digite uma frase: ")
    minha_biblioteca.imprimir_com_pausa(frase)

if __name__ == "__main__":
    main()
