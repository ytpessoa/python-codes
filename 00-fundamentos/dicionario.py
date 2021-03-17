

#dicionario: chave, valor


>>> pessoa = { 'nome': 'Profa. Ana', 'idade': 38, 'cursos': ['Ingles', 'Portugues'] }

>>> type(pessoa)
<class 'dict'>

>>> dir(pessoa)
['__class__', '__class_getitem__', '__contains__', '__delattr__', '__delitem__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', 
'__getattribute__', '__getitem__', '__gt__', '__hash__', '__init__', '__init_subclass__', '__ior__', '__iter__', '__le__', '__len__', 
'__lt__', '__ne__', '__new__', '__or__', '__reduce__', '__reduce_ex__', '__repr__', '__reversed__', '__ror__', '__setattr__', '__setitem__',
 '__sizeof__', '__str__', '__subclasshook__', 'clear', 'copy', 'fromkeys', 'get', 'items', 'keys', 'pop', 'popitem', 'setdefault', 'update', 'values']

#Acessando pelas chaves
 >>> pessoa['nome']
'Profa. Ana'
>>> pessoa['idade']
38
>>> pessoa['cursos']
['Ingles', 'Portugues']
>>>


>>> pessoa.keys()
dict_keys(['nome', 'idade', 'cursos'])
>>> pessoa.values()
dict_values(['Profa. Ana', 38, ['Ingles', 'Portugues']])
>>>

>>> pessoa.clear()
>>> pessoa
{}

