#Escreva uma função que receba um float representando o
#valor da temperatura em Celsius e retorne a temperatura
#equivalente em Farenheit. Em seguida, escreva um código
#que leia uma temperatura em Celsius e informe o valor
#equivalente em Farenheit.

#Celsius para Farenheit => T(f) = T(c) x 9/5 + 32
#Farenheit para Celsius => T(c) = (T(f) - 32) x 5/9

def menu_inicial():
    print('Programa para Conversão de Temperaturas')
    print('1. Converte de Celsius para Fahrenheit')
    print('2. Converte de Fahrenheit para Celsius')

#Celsius para Farenheit
def celsius_to_farenheit():
    C = float(input('Valor da temperatura em graus Celsius: '))
    F = C * (9 / 5) + 32
    print('Valor em Fahrenheit: {0}°F'.format(F))
#It's an indicator to the format method that you want it to be replaced 
#by the first (index zero) parameter of format. (eg "2 + 2 = {0}".format(4))

#Farenheit para Celsius
def farenheit_to_celsius():
    F = float(input('Valor da temperatura em graus Fahrenheit: '))
    C = (F - 32) * (5 / 9)
    print('Valor em Celsius: {0}°C'.format(C))


menu_inicial()
escolha = input('Escolha o tipo de conversão que deseja realizar: ')

if escolha == '1':
    celsius_to_farenheit()

if escolha == '2':
    farenheit_to_celsius()



