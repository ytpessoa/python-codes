

#String é imutável
s = "1,2,3"
print( s[0] )
#1
print (dir(str))
# ['__add__', '__class__', '__contains__', '__delattr__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', 
# '__getitem__', '__getnewargs__', '__gt__', '__hash__', '__init__', '__init_subclass__', '__iter__', '__le__', '__len__', '__lt__',
#  '__mod__', '__mul__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__rmod__', '__rmul__', '__setattr__', '__sizeof__', 
#  '__str__', '__subclasshook__', 'capitalize', 'casefold', 
# 'center', 'count', 'encode', 'endswith', 'expandtabs', 'find', 'format', 'format_map', 'index', 'isalnum', 'isalpha', 'isascii', 
# 'isdecimal', 'isdigit', 'isidentifier', 'islower', 'isnumeric', 'isprintable', 'isspace', 'istitle', 'isupper', 'join', 'ljust', 
# 'lower', 'lstrip', 'maketrans', 'partition', 'removeprefix', 'removesuffix', 'replace', 'rfind', 'rindex', 'rjust', 'rpartition', 
# 'rsplit', 'rstrip', 'split', 'splitlines', 'startswith', 'strip', 'swapcase', 'title', 'translate', 'upper', 'zfill']


#String multiplas linhas

doc = """Texto com multiplas
linhas definindo um doc."""
print (doc)
# Texto com multiplas
# linhas definindo um doc.


# indices da String:
#    0  1  2   frente pra trás
#   -3 -2 -1   trás pra frente

s = "1,2,3"
print( s[-1] )
#3
print( s[1:] ) 
#,2,3
#
s = "0123456789"
print( s[::] ) # :: -> inicio ao fim
#1234567890
print( s[::2] ) #de 2 em 2
#02468
print( s[4::2] ) #comeca em 4 e de 2 em 2
#468
print( s[::-1] ) #de 1 em 1 de tras pra frente
#9876543210
print( s[::-2] ) #de 2 em 2 de tras pra frente
#97531



frase = "Python eh uma linguagem excelente!"
print( "eh" in frase )
#True
print( "ytallo" not in frase )
#True
print( len(frase) ) 
#34
print( "py" in frase )
#False
print( "py" in frase.lower() ) #nao modifica a string original
#True

frase = frase.upper()
print(frase)
#PYTHON EH UMA LINGUAGEM EXCELENTE!
print( frase.split() )
#['PYTHON', 'EH', 'UMA', 'LINGUAGEM', 'EXCELENTE!']

print( dir(str)   )



