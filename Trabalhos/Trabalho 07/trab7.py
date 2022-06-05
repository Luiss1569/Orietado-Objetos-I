from abc import ABC, abstractmethod

class Venda:
    def __init__(self, codImovel, mesVenda, anoVenda, valorVenda):
        self.__codImovel = codImovel
        self.__mesVenda = mesVenda
        self.__anoVenda = anoVenda
        self.__valorVenda = valorVenda
        
    def getCodImovel(self):
        return self.__codImovel
    
    def getMesVenda(self):
        return self.__mesVenda
    
    def getAnoVenda(self):
        return self.__anoVenda
    
    def getValorVenda(self):
        return self.__valorVenda 
        

class Funcionario(ABC):
    def __init__(self, codigo, nome):
        self.__nome = nome
        self.__codigo = codigo
        self.__vendas = []
        
    def getCodigo(self):
        return self.__codigo
    
    def getNome(self):
        return self.__nome
    
    def getVendas(self):
        return self.__vendas
    
    def adicionaVenda(self,pCodImovel, pMes, pAno, pValor):
        venda = Venda(pCodImovel, pMes, pAno, pValor)
        self.__vendas.append(venda)
        
    @abstractmethod
    def getDados():
        pass
    
    @abstractmethod
    def calculaRenda():
        pass
    
class Contratado(Funcionario):
    def __init__(self, codigo, nome, pSalario, pNuroCartTrab):
        super().__init__(codigo, nome)
        self.__nroCartTrabalho = pNuroCartTrab
        self.__salario = pSalario
        
    def getNroCartTrab(self):
        return self.__nroCartTrabalho
    
    def getDados(self):
        return "Nome: " + self.getNome() + " - Nro Carteira:" + str(self.getNroCartTrab())
        
    def getSalarioFixo(self):
        return self.__salario
        
    def calculaRenda(self, pMes, pAno):
        comissao = 0
        for venda in self.getVendas():
            if venda.getMesVenda() is pMes and venda.getAnoVenda() is pAno:
                comissao += venda.getValorVenda() * (1/100) 
            
        return self.__salario + comissao
        
class Comissionado(Funcionario):
    def __init__(self, codigo, nome, pNroCPF, pComissao):
        super().__init__(codigo, nome)
        self.__nroCPF = pNroCPF
        self.__comissao = pComissao
        
    def getNroCPF(self):
        return self.__nroCPF
    
    def getDados(self):
        return "Nome: " + self.getNome() + "- Nro CPF: " +  str(self.getNroCPF())
        
    def getComissao(self):
        return self.__comissao
        
    def calculaRenda(self, pMes, pAno):
        comissao = 0
        for venda in self.getVendas():
            if venda.getMesVenda() is pMes and venda.getAnoVenda() is pAno:
                comissao += venda.getValorVenda() * (self.__comissao/100)
            
        return comissao       

if __name__ == "__main__":
    funcContratado = Contratado(1001, 'João da Silva', 2000, 1234)
    funcContratado.adicionaVenda(100, 3, 2022, 200000)
    funcContratado.adicionaVenda(101, 3, 2022, 300000)
    funcContratado.adicionaVenda(102, 4, 2022, 600000)
    funcComissionado = Comissionado(1002, 'José Santos', 4321, 5)
    funcComissionado.adicionaVenda(200, 3, 2022, 200000)
    funcComissionado.adicionaVenda(201, 3, 2022, 400000)
    funcComissionado.adicionaVenda(202, 4, 2022, 500000)
    listaFunc = {funcContratado, funcComissionado}
    for func in listaFunc:
        print (func.getDados())
        print ("Renda no mês 3 de 2022: ")
        print (func.calculaRenda(3, 2022))