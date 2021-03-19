
#constantes com letra maiuscula
PALAVRAS_PROIBIDAS = ('futebol', 'religiao', 'politica')
frases = [
    'Joao gosta de futebol e politica',
    'A praia foi divertida',

]

for frase in frases: 
    for palavra in frase.lower().split():
        if palavra in PALAVRAS_PROIBIDAS:
            print(f"texto possui a palavra {palavra.upper()} que eh proibida!")         
            break    
    else: #parado pelo break tambem
        print("Texto autorizado!")
