#for: quantidade determinada de repeticoes


#percorrendo dicionario

produto = {'nome': 'Caneta chic', 'preco':'14.99' ,
           'importada': True , 'estoque': 793}

#por padrao percorre as chaves 
for chave in produto:
    print(f'{chave}')

for valor in produto.values():
    print(f'{valor}')

for chave, valor in produto.items():
    print(f'{chave}:{valor}')