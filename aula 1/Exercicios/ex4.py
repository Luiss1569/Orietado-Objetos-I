#Utilizando a tabela a seguir, escreva um código que permita
#obter a alíquota do imposto de renda de acordo com o valor da
#renda mensal. Seu programa deve ler o valor da renda e
#imprimir o valor da alíquota, bem como o valor do imposto a
#pagar.
#Renda                     Alíquota
#De 1.903,99 até 2.826,65  7,5%
#De 2.826,66 até 3.751,05  15%
#De 3.751,06 até 4.664,68  22,5%
#Acima de 4.664,68         27,5%

valor_renda = float(input("Valor da sua renda: R$ "))
if valor_renda <= float(1903.99):
    valor_aliquota = 0.0
    print('Valor da aliquota: ' + '0')
    valor_imposto = valor_renda * valor_aliquota
    print('Valor do imposto: ' + str(valor_imposto))
elif valor_renda > float(1903.99) and valor_renda <= float(2826.65):
    valor_aliquota = 0.075
    print('Valor da aliquota: ' + '7,5%')
    valor_imposto = valor_renda * valor_aliquota
    print('Valor do imposto: ' + str(valor_imposto))
elif valor_renda >= float(2826.66) and valor_renda <= float(3751.05):
    valor_aliquota = 0.15
    print('Valor da aliquota: ' + '15%')
    valor_imposto = valor_renda * valor_aliquota
    print('Valor do imposto: ' + str(valor_imposto))
elif valor_renda >= float(3751.06) and valor_renda <= float(4664.68):
    valor_aliquota = 0.225
    print('Valor da aliquota: ' + '22,5%')
    valor_imposto = valor_renda * valor_aliquota
    print('Valor do imposto: ' + str(valor_imposto))
else:
    valor_aliquota = 0.275
    print('Valor da aliquota: ' + '27,5%')
    valor_imposto = valor_renda * valor_aliquota
    print('Valor do imposto: ' + str(valor_imposto))

#print(valor_renda)
#print(valor_aliquota)

