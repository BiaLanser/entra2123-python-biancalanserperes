from mydefs import name, entra21, math
from env import API_KEY

def main():
    print(name, '\n'+ entra21('aaa')) # 'aaa' é argumento de word(mydefs)
    print(math(5, 6))
   
if __name__ == '__main__': #padrão de main
    main()