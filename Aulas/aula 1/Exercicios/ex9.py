#Escreva uma função booleana que recebe uma string e
#verifica se a mesma é um palíndromo. Em seguida, escreva
#um código para ler uma string e, usando a função criada,
#verifique se a mesma é uma string.

def palíndromo(string1, string2s):
    palavra_sem_espacos = string1.replace(' ', '')
    palavra_toda_minuscula = palavra_sem_espacos.lower()
    #print(palavra_toda_minuscula)
    invertida = palavra_toda_minuscula[::-1]
    #print(is_or_not_palíndromo)s
    if invertida == palavra_toda_minuscula:
        print('Sim, é um palíndromo')
    else:
        print('Não, não é um palíndromo')

    is_string = type(string2s)
    print('É: ' + str(is_string))
    

palavra = input('Digite uma palavra: ')
string = input('Digite uma string: ')
palíndromo(palavra, string)
