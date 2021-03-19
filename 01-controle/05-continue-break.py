

for i in range(1,11):
    if i % 2 == 0:
        continue #associado ao "for"  e não ao "if".
                 #interrompe a repeticao corrente e vai pra próxima.
    print(i)


for i in range(1,11):
    if i % 2 == 0:
        break #associado ao "for"  e não ao "if".
              #sai do laço "for" e nao do programa
    print(i)