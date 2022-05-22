#Leia valores numéricos e os coloque numa lista. A leitura
#termina quando o valor 0 for digitado. Em seguida,
#calcule a média dos valores digitados e informe o
#usuário.

print('Digite um número por vez, quando não quiser adionar mais números digite 0.')
entrada = 1
lista = []
while entrada != 0:
    entrada = int(input('Número: '))
    if entrada != 0:
        lista.append(entrada)

print(lista)
média = sum(lista) / len(lista)
print('A média é ' + str(média))