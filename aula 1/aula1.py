#IMPORTS    
import os
import random # importanto pacote para número randomico
from datetime import datetime, timedelta #para datas, timedelta é usado para definir um período de tempo
from array import array #import de array


#rodando no cmd:
#cd /d D:\Downloads 
#na pasta que contem o arquivo digite python e o nome do file = python aula1.py 

#print
print('Hello world')
print('Hello world com aspas simples')
print("Hello world com aspas duplas")
#print de linha vazia
print()
#print cm quebra de linha
print('Quebra de linha \nno meio de uma string')
print("It's a small world after all")

#Escreva seu nome
name = input('Seu nome: ')
print(name)
sobrenome = input('Seu sobrenome: ')
print(sobrenome)
print('Olá ' + name + ' ' + sobrenome)
frase = 'Olá ' + name + ' ' + sobrenome
print(frase.upper())
print(frase.lower())
print(frase.capitalize())
print(frase.count('a'))
print('Olá ' + name.capitalize() + ' ' + sobrenome.capitalize())
have_or_not = 'dio' in frase
print(have_or_not)

#números
pi = 3.14159
print(pi)

#Deve-se converter números em strings para permitir concateção
dias_fev = 28
print(str(dias_fev) + ' dias em Fevereiro')
#28 dias em Fevereiro

#A função input sempre retorna strings
num1 = input('Digite o primeiro número: ')
num2 = input('Digite o segundo número: ')
print (num1 + num2)
#56

#Números armazenados como strings precisam ser
#convertidos para números a fim de que seja possível
#realizar operações matemáticas
num1 = input('Digite o primeiro número: ')
num2 = input('Digite o segundo número: ')
print (int(num1) + int(num2))
print (float(num1) + float(num2))
#11
#11.0

#número randomico
print(random.randrange(1,10))

#datas
data_corrente = datetime.now()
# a função now retorna um objeto datetime
print('Hoje é: ' + str(data_corrente))
#Hoje é: 2020-02-07 16:17:18.694511

data_corrente = datetime.now()
print('Hoje é: ' + str(data_corrente))
#Hoje é: 2020-02-07 16:17:18.694511
um_dia = timedelta(days=1)
ontem = data_corrente - um_dia
print('Ontem foi: ' + str(ontem))
#Ontem foi: 2020-02-06 16:17:18.694511
print('Dia: ' + str(data_corrente.day))
print('Mês: ' + str(data_corrente.month))
print('Ano: ' + str(data_corrente.year))
#Dia: 7
#Mês: 2
#Ano: 2020
nasc = input('Informe data nasc (dd/mm/yyyy): ')
data_nasc = datetime.strptime(nasc, '%d/%m/%Y') #isso aqui é para converter em dia, mês e ano
print ('Nacimento: ' + str(data_nasc))
#Informe data nasc (dd/mm/yyyy): 24/04/1998
#Nascimento: 1998-04-24 00:00:00
um_dia = timedelta(days=1)
vespera_nasc = data_nasc - um_dia
print('Véspera do nascimento: ' + str(vespera_nasc))
#Véspera do nascimento: 1998-04-23 00:00:00


#if else
#if renda >= 1900:
#    imposto = 7.5
#    print(imposto)

#if renda >= 1900:
#    imposto = 7.5
#    print(imposto)
#else:
#    imposto = 0
#    print imposto

#if estado == 'SP':
#    frete = 10
#if estado == 'RJ':
#    frete = 10
#if estado == 'MG':
#    frete = 15
#if estado == 'ES':
#    frete = 18

#Se apenas uma condição pode ocorrer, é possível usar um
#único if em conjunto com um ou mais elif’s
#if estado == 'SP':
#    frete = 10
#elif estado == 'RJ':
#    frete = 10
#elif estado == 'MG':
#    frete = 15
#elif estado == 'ES':
#    frete = 18
#else:
#    frete = 2

#com in 
#if estado in('SP', 'RJ', 'PR'):
#    frete = 10
#elif estado == 'MG':
#    frete = 15
#elif estado == 'ES':
#    frete = 18
#else:
#    frete = 20

#if estado in('SP', 'RJ', 'PR') and cupom:
#    frete = 0
#(Aqui estamos considerando que cupom é uma variável booleana)


#listas são coleções de itens
nomes = ['Pedro', 'Marina']
notas = []
notas.append(9.2) # Adiciona novo item no final
notas.append(8.4)
print(nomes)
print(notas)
print(notas[1]) # Coleções iniciam no zero
#['Pedro', 'Marina']
#[9.2, 8.4]
#8.4

#Arrays também são coleções de itens
notas = array('d')
notas.append(9.2)
notas.append(8.4)
print(notas)
print(notas[1])
#array('d', [9.2, 8.4])
#8.4

#array Armazenam tipos simples como números Todos os itens devem ser do mesmo tipo
#lista Armazenam qualquer dado De qualquer tipo
nomes = ['Pedro', 'Marina']
print(len(nomes)) # Obtém o número de itens
nomes.insert(0, 'Beto') # Insere antes do índice
print(nomes)
nomes.sort()
print(nomes)
#2
#['Beto', 'Pedro', 'Marina']
#['Beto', 'Marina', 'Pedro']

nomes = ['Pedro', 'Marina', 'Beto']
alunos = nomes[0:2] # Obtém os dois primeiros itens
# Índice inicial e número de itens a recuperar
print(nomes)
print(alunos)
#['Pedro', 'Marina', 'Beto']
#['Pedro', 'Marina']

pessoa = {'nome': 'Pedro'}
pessoa['sobrenome'] = 'Souza'
print(pessoa )
print(pessoa ['nome'])
#{'nome': 'Pedro', 'sobrenome': 'Souza'}
#Pedro

#dicionario pares chave / valor Ordem de armazenamento não garantido
#Listas Baseado em índice (inicia no 0) Ordem de armazenamento garantida

#lista = []
#um array pode guardar uma lista dentro = {a, [1, 2]}

#Laços
for nome in ['Pedro', 'Marina', 'Beto']:
    print(nome)
#Pedro
#Marina
#Beto

for index in range(0, 2):
    print(index)
#0
#1

nomes = ['Pedro', 'Marina', 'Beto']
index = 0
while index < len(nomes):
    print(nomes[index])
    # Muda a condição
    index = index + 1
#Pedro
#Marina
#Beto

# Strings são listas de caracteres
for x in 'Ana':
    print(x)
#A
#n
#a

#Funções
nome = 'Pedro'
print('Tarefa concluída')
print(datetime.datetime.now())
print()
for x in range(0,10):
    print(x)
print('Tarefa concluída')
print(datetime.datetime.now())
print()

#Função para não haver repetição de código 
def print_time():
    print('Tarefa concluída')
    print(datetime.datetime.now())
    print()
nome = 'Pedro'
print_time()
for x in range(0,10):
    print(x)
print_time()

#passando o nome que vai ser printado como parãmetro
def print_time(nome_tarefa):
    print(nome_tarefa)
    print(datetime.now())
    print()
nome = 'Pedro'
print_time('Nome atribuído')
for x in range(0,10):
    print(x)
print_time('Loop executado')

#exercicio de aula
#Vamos agora implementar uma função que receba uma string e
#retorne sua primeira letra. Utilizando essa função, vamos escrever
#um código que leia um nome e imprima as iniciais do nome lido.
def get_inicial(str):
    inicial = str[0:1] #maiusculo inicial = str[0:1].upper()
    return inicial
nome = input('Digite seu nome: ')
inicial_nome = get_inicial(nome)
sobrenome = input('Digite seu sobrenome: ')
inicial_sobrenome = get_inicial(sobrenome)
print('Suas iniciais são: ' + inicial_nome + inicial_sobrenome)
#Digite seu nome: Pedro
#Digite seu sobrenome: Souza
#Suas iniciais são: ps

#função com multiplo parâmetros
def get_inicial(str, maiuscula):
    if maiuscula:
        inicial = str[0:1].upper()
    else:
        inicial = str[0:1]
    return inicial
nome = input('Digite seu nome: ')
inicial_nome = get_inicial(nome, False)
print('Sua inicial é: ' + inicial_nome)
#Digite seu nome: Pedro
#Sua inicial é: p

#é possível especificar um valor default para um parâmetro
def get_inicial(str, maiuscula=True):
    if maiuscula:
        inicial = str[0:1].upper()
    else:
        inicial = str[0:1]
    return inicial
nome = input('Digite seu nome: ')
inicial_nome = get_inicial(nome)
print('Sua inicial é: ' + inicial_nome)
#Digite seu nome: Pedro
#Sua inicial é: P

#posso especificar aqui tambem
inicial_nome = get_inicial(maiuscula=True, str=nome)
#Quando os parâmetros são nomeado, eles podem aparecer em qualquer ordem



#debbug de erro com print
#print('Adicionando números')
#x = 42 + 206
#print('Realizando divisão')
#y = x / 0
#print('Operação concluída')

#erro de numeros
#A combinação de strings com números não é permitida
#dias_fev = 28
#print(dias_fev + ' dias em Fevereiro')
