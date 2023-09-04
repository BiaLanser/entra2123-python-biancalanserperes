import time

def imprimir_com_pausa(frase):
    for caractere in frase:
        if caractere != ' ':
            print(caractere)
            time.sleep(1)
        else:
            print("\n")
