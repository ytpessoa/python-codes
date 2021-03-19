
#constantes com letra maiuscula
PALAVRAS_PROIBIDAS = {'futebol', 'religiao', 'politica'} #set
frases = [
    'Joao gosta de futebol e politica',
    'A praia foi divertida',

]

for frase in frases:
    setFrase = set(frase.lower().split())
    intersecao = PALAVRAS_PROIBIDAS.intersection(setFrase)
    if intersecao:
        print(f"texto possui palavra proibida {intersecao}")
    else:
        print("Texto autorizado!")



