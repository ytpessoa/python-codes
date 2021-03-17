
# is
x = 3
y = x
z = 3

print ( x is y ) #True

# is not
print ( x is not z ) #False


lista1 = [1,2,3] #ponteiro -> [1,2,3]¹
lista2 = lista1  #ponteiro -> [1,2,3]¹
lista3 = [1,2,3] #ponteiro -> [1,2,3]²

print (lista1 is lista2) #True
print (lista1 is lista3) #False