import argparse
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
    parser = argparse.ArgumentParser(description="Gerador de Senhas Aleatórias")
    parser.add_argument("comprimento", type=int, help="Comprimento da senha")
    parser.add_argument("--letras-min", action="store_true", help="Incluir letras minúsculas")
    parser.add_argument("--letras-mai", action="store_true", help="Incluir letras maiúsculas")
    parser.add_argument("--numeros", action="store_true", help="Incluir números")
    parser.add_argument("--especiais", action="store_true", help="Incluir caracteres especiais")
    
    args = parser.parse_args()
    
    senha = gerar_senha(args.comprimento, args.letras_min, args.letras_mai, args.numeros, args.especiais)
    
    print("\nSenha gerada:", senha)

if __name__ == "__main__":
    main()
    
"""
Para Executar:
python gex003b.py 12 --letras-min --numeros
"""
