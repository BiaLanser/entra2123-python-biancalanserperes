from mydefs import name
from env import API_KEY
from mydefs import entra21
from mydefs import math

def main():
    print(name, '\n'+ entra21('aaa')) # 'aaa' é argumento de word(mydefs)
    print(math(5, 6))
   
if __name__ == '__main__': #padrão de main
    main()