



# Lista eh um objeto mutavel, heterogenea e indexada


# lista.metodo() --> altera "lista"

>>> lista = [1,2,3,4,5]

>>> lista.remove(4)
>>> lista
[1, 2, 3, 5]

>>> lista.index(3)
2


>>> del lista[2] # 2 indice
>>> lista
[1, 2, 5]