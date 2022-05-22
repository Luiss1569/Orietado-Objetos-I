import random
import time

RANDOM_QUANTIDADE = 5000
RANDOM_INICIO = 1
RANDOM_FIM = 20000


def partition(array, start, end):
    pivot = array[start]
    low = start+1
    high = end
    
    while True:
        while low <= high and array[high] >= pivot:
            high = high - 1
        while low <= high and array[low] <= pivot:
            low = low + 1
        if low <= high:
            array[low], array[high] = array[high], array[low]
        else:
            break
    array[start], array[high] = array[high], array[start]
    
    return high

def quickSort(array, start, end):
    if start>= end:
        return
    p = partition(array, start, end)
    quickSort(array, start, p-1)
    quickSort(array, p+1, end)
    
    
def bubbleSort(array):
    for i in range(len(array)):
        for j in range(len(array)-1-i):
            if array[j] > array[j+1]:
                array[j], array[j+1] = array[j+1], array[j]


def randomArray(quantidade, inicio, fim):
    array = []
    for i in range(quantidade):
        array.append(random.randint(inicio, fim))
    return [array, array.copy()]
                
def main():
    [array, arrayCopy] = randomArray(RANDOM_QUANTIDADE, RANDOM_INICIO, RANDOM_FIM)
    
    inicio = time.time()
    quickSort(array, 0, len(array)-1)
    fim = time.time()
    print(f"quickSort: {fim - inicio}")
    
    inicio = time.time()
    bubbleSort(arrayCopy)
    fim = time.time()
    print(f"bubbleSort: {fim - inicio}")
    
main()
    
