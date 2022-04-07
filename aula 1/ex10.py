from datetime import datetime, timedelta
from time import strftime, gmtime
#Escreva uma função que receba como parâmetros valores de
#horas, minutos e segundos representando a duração de um
#evento e retorne o valor da duração totalizado em segundos.

#Escreva uma função que transforme um valor de duração
#totalizado em segundos, para horas, minutos e segundos.

#Escreva um programa que leia hora, minuto e segundo de
#entrada e de saída de um usuário na internet e, utilizando as
#funções de conversão, mostre na tela em horas, minutos e
#segundos o tempo que o usuário ficou conectado. Desconsidere a
#hipótese de que a desconexão tenha ocorrido após a meia-noite.

def em_segundos(horas, minutos, segundos):
    horas_segundos = horas * 3600
    minutos_segundos = minutos * 60
    print('Total de segundos é {0}'.format(horas_segundos + minutos_segundos + segundos))

def em_horas_minutos_segundos(segundos_total):
    #min, sec = divmod(segundos_total, 60) 
    #hour, min = divmod(min, 60) 
    #print("Hora: %d:%02d:%02d" % (hour, min, sec))
    print('Hora: ' + str(timedelta(seconds = segundos_total)))
    print('Hora: ' + strftime("%H:%M:%S", gmtime(segundos_total))) 

def horario_total(hora1, hora2):
    time1 = datetime.strptime(hora1,"%H:%M:%S")
    time2 = datetime.strptime(hora2,"%H:%M:%S")
    time_interval = time2 - time1
    print ('Tempo que você ficou conectado: ' + str(time_interval))
    
print("Escreva a duração do evento apenas com números.")
horas = int(input('Horas: '))
minutos = int(input('Minutos: '))
segundos = int(input('Segundos: '))

em_segundos(horas, minutos, segundos)

print("Escreva a duração do evento em segundos (apenas números).")
segundos_total = int(input('Segundos: '))

em_horas_minutos_segundos(segundos_total)

print("Escreva a dois horarios (00:00:00).")
hora1 = input('Hora 1: ')
hora2 = input('Hora 2: ')

horario_total(hora1, hora2)
