

# tupla = (element1, elemento2) -> imutavel
# lista = [elemento, elemento2] -> mutavel

# tupla: sequencia imutavel, indexada!

>>> tupla2 = ()
>>> type(tupla2)
<class 'tuple'>

#tupla 1 elemento
>>> tupla = ('uma',)
>>> type(tupla)
<class 'tuple'>

>>> tupla[0]
'uma'

>>> tupla[0] = 'novo'
TypeError: 'tuple' object does not support item assignment