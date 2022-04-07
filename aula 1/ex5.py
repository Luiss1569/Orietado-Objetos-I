#Leia um conjunto de nomes e os armazene numa lista. Em
#seguida, leia um nome e verifique se o mesmo faz parte
#dessa lista.

total = int(input('Quantos nomes você irá adicionar? '))
print(total)
i = 0
lista = []
while i < total:
  nome = input('Nome: ')
  lista.append(nome)
  i += 1
print(lista)
verificar = input('Qual nome você quer verificar na lista? ')
have_or_not = verificar in lista
print('O nome existe na lista? ' + str(have_or_not))