import random # importanto pacote
print(random.randrange(1,10))

#Leia dois números correspondentes a um intervalo, gere e
#imprima um número randômico dentro desse intervalo
first = input('Primeiro número: ')
#print(first)
second = input('Segundo número: ')
#print(second)
#print(type(first))
#print(type(second))
#Da para redeclarar em python
first = int(first)
#print(type(first))
second = int(second)
#print(type(second))
print(random.randrange(first,second))
