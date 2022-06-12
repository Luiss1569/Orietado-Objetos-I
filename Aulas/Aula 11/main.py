def mdc(m, n):
    while m%n != 0:
        oldm = m
        oldn = n
        m = oldn
        n = oldm%oldn
    return n

def mesmaFracao(f1, f2):
    return (f1.getNum() == f2.getNum()) and (f1.getDen() == f2.getDen())


class Fracao():
    
    def __init__(self, num, den):
        self.__num = num        
        self.__den = den     

    def __str__(self):
        return str(self.__num) + "/" + str(self.__den)

    def getNum(self):
        return self.__num

    def getDen(self):
        return self.__den       

    def simplifica(self):
        divComum = mdc(self.__num, self.__den)
        self.__num = self.__num // divComum
        self.__den = self.__den // divComum   

    def __add__(self,outraFrac):
        novoNum = self.__num * outraFrac.getDen() + self.__den * outraFrac.getNum()
        novoDen = self.__den * outraFrac.getDen()
        divComum = mdc(novoNum, novoDen)
        novoNum = self.__num // divComum
        novoDen = self.__den // divComum

        if(novoNum >= novoDen):
            novoInt = novoNum // novoDen
            novoNum = novoNum* novoInt - novoNum
            
        
        return Fracao(novoNum//divComum, novoDen//divComum)  

class FracaoMista():
    
    def __init__(self, int, num, den):
        self.__int = int
        self.__num = num        
        self.__den = den     

    def __str__(self):
        return str(self.__int) + " + " +  str(self.__num) + "/" + str(self.__den)

    def getInt(self):
        return self.__int
    
    def getNum(self):
        return self.__num

    def getDen(self):
        return self.__den       

    def simplifica(self):
        divComum = mdc(self.__num, self.__den)
        self.__num = self.__num // divComum
        self.__den = self.__den // divComum   

    def __add__(self,outraFrac):
        novoNum = self.__num * outraFrac.getDen() + self.__den * outraFrac.getNum()
        novoDen = self.__den * outraFrac.getDen()
        divComum = mdc(novoNum, novoDen)
        resultNum = novoNum // divComum
        resultDen = novoDen // divComum
        novoInt = self.__int
        novoInt += resultNum // resultDen
        
        if resultNum > resultDen:
            resultNum = resultNum % resultDen
        
        if(type(outraFrac) is FracaoMista):
            novoInt += outraFrac.getInt()
            
        if resultNum ==  resultDen:
            return novoInt
        
        return FracaoMista(novoInt, resultNum, resultDen)
             

if __name__ == "__main__":
    frac1 = Fracao (1, 4) 
    frac2 = Fracao(1, 6)
    frac3 = frac1 + frac2
    #print(frac3)
    #print()
    frac1 = Fracao (3, 4)
    frac2 = Fracao(5, 6)
    frac3 = frac1 + frac2
    #print(frac3)

    frac4 = FracaoMista(1,1,3)
    #print(frac4)
    
    frac5 = FracaoMista(2, 1, 3)
    frac6 = frac4 + frac5
    print(frac6)