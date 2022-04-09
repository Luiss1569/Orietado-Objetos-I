#Leia uma data no passado e informe em qual dia da
#semana essa data caiu.
from datetime import datetime, timedelta #para datas, timedelta é usado para definir um período de tempo

data = input('Informe uma data do passado (dd/mm/yyyy): ')
data_pass = datetime.strptime(data, '%d/%m/%Y') #isso aqui é para converter em dia, mês e ano
print ('Dia: ' + str(data_pass))
um_dia_antes = timedelta(days=1)
vespera = data_pass - um_dia_antes
print('Véspera da data: ' + str(vespera))
print(data_pass.strftime("Dia da semana: %A"))