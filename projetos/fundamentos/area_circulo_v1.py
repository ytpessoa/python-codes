
import math 
import sys

class TerminalColor:
    ERRO = '\033[91m' #cor vermelha
    NORMAL = '\033[0m' #cor normal

def circulo(raio):
    return pi * raio ** 2

def help():
    print(f"Necessario: python {sys.argv[0]} <raio>")

if __name__ == '__main__': # modulo "main"
    
    #> python area_circulo_v1.py 12.4
    #print(sys.argv[0]) # area_circulo_v1.py
    #print(sys.argv[1]) # 12.4
    
    if( len(sys.argv) < 2 ): 
        help()
        sys.exit(1) #0:sucesso, 1,2...:erro
    
    if not sys.argv[1].isnumeric():
        help()
        print(
            TerminalColor.ERRO + "O raio deve ser numerico" + 
            TerminalColor.NORMAL
        )
        sys.exit(2)
    
    
    pi = math.pi   
    raio = float(sys.argv[1])
    resultado = circulo(raio)
    print(resultado)

# > python


# >>> dir() 
# ['__annotations__', '__builtins__', '__doc__', '__loader__', 
# '__name__', '__package__', '__spec__']

# print(f"Nome do modulo {__name__}")
# __main__
# >python
# >>> import area_circulo_v1
# >>> dir()
# ['__annotations__', '__builtins__', '__doc__', '__loader__',
#  '__name__', '__package__', '__spec__', 'area_circulo_v1']

