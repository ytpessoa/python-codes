

import sys

def conceito(valor):
    nota = float(valor)

    if nota > 10:
        return 'Nota Invalida' 
    elif nota >= 9.1: # entre 10 e 9.1
        return "A"
    elif nota >= 8.1: # entre 9.1 e 8.1
        return "A-"
    elif nota >= 7.1: # entre 8.1 e 7.1
        return "B"
    elif nota >= 0: # entre 7.1 e 0  
        return "E-"
    else: # entre 0 e negativo
        return "Nota negativa eh invalida"




def help():
    print(f"Entrada correta: python {sys.argv[0]} <n1> <n2>")



if __name__ == "__main__":
    notaAluno = input("Nota do aluno: ")
    conceito = conceito(notaAluno)
    print(conceito)
    if(len(sys.argv) < 4):
        help()