

#set : apenas valores, não aceita repeticao, não garante ordem de insercao, nao indexado


>>> conjunto = {1,2,3}

>>> type(conjunto)
<class 'set'>


>>> conjunt2 = set('aabbcc')
>>> conjunt2
{'c', 'a', 'b'}

>>> 'c' in conjunt2
True
>>> 'z' not in conjunt2
True


>>> {1,2,3} == {3,2,1,3,1,2}
True


>>> c1 = {1,2}
>>> c2 = {2,3}
>>> dir(c1)
# ['__and__', '__class__', '__class_getitem__', '__contains__', '__delattr__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__',
#  '__getattribute__', '__gt__', '__hash__', '__iand__', '__init__', '__init_subclass__', '__ior__', '__isub__', '__iter__', '__ixor__', 
#  '__le__', '__len__', '__lt__', '__ne__', '__new__', '__or__', '__rand__', '__reduce__', '__reduce_ex__', '__repr__', '__ror__', '__rsub__',
#   '__rxor__', '__setattr__', '__sizeof__', '__str__', '__sub__', '__subclasshook__', '__xor__', 'add', 'clear', 'copy', 'difference', 'difference_update', 'discard',
#    'intersection', 'intersection_update', 'isdisjoint', 'issubset', 'issuperset', 'pop', 'remove', 'symmetric_difference', 'symmetric_difference_update', 'union', 'update']
>>> c1.union(c2)
{1, 2, 3}

#subconjunto
>>> c2 <= c1
False

#diferenca
>>> c1 - c2
{1}


# atribuicao subtrativa
>>> c1
{1, 2}
>>> c1 -= {2}
>>> c1
{1}
>>>



