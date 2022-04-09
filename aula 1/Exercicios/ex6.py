#Leia uma string e verifique se a mesma é um
#palíndromo

#Podemos verificar se há strings do Palíndromo revertendo a string original e 
#comparando cada elemento da string original com cada elemento da string invertida; 
#isso pode ser feito com o fatiamento da lista. 
palavra = input('Digite a palavra para verificar se é palíndromo: ')
#Primeiro calculamos o valor reverso da palavra original com [::-1] como o índice da lista. 
#Em seguida, comparamos cada índice com o operador de igualdade ==.
if str(palavra) == str(palavra)[::-1] :
    print("Palíndromo")
else:
    print("Não palíndromo")