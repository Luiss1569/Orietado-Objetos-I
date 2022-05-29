from abc import ABC, abstractmethod

class PontoFunc():
    def __init__(self, mes, ano, nroFaltas, nroAtrasos):
        self.__mes = mes
        self.__ano = ano
        self.__nroFaltas = nroFaltas
        self.__nroAtrasos = nroAtrasos

    def getMes(self):
        return self.__mes

    def getAno(self):
        return self.__ano

    def getNroFaltas(self):
        return self.__nroFaltas

    def getNroAtrasos(self):
        return self.__nroAtrasos

    def lancaFaltas(self, nroFaltas):
        self.__nroFaltas += nroFaltas

    def lancaAtrasos(self, nroAtrasos):
        self.__nroAtrasos += nroAtrasos   

class Funcionario(ABC):
    def __init__(self, codigo, nome):
        self.__codigo = codigo
        self.__nome = nome
        self.__pontoMensal = []

    def getCodigo(self):
        return self.__codigo

    def getNome(self):
        return self.__nome

    def getPontoMensal(self):
        return self.__pontoMensal

    def adicionaPonto(self, mes, ano, faltas, atrasos):
        nPonto = PontoFunc(mes, ano, faltas, atrasos)
        self.__pontoMensal.append(nPonto)

    def lancaFaltas(self, mes, ano, faltas):
        for folha in self.__pontoMensal:
            if (folha.getMes() == mes and folha.getAno() == ano):
                folha.lancaFaltas(faltas)
                return

    def lancaAtrasos(self, mes, ano, atrasos):
        for folha in self.__pontoMensal:
            if (folha.getMes() == mes and folha.getAno() == ano):
                 folha.lancaAtrasos(atrasos)
                 return

    def imprimeFolha(self, mes, ano):
        print(f"Código:{self.__codigo}")
        print(f"Nome:{self.__nome}")
        print("Salario Liquido:{:.2f}".format(self.calculaSalario(mes, ano)))
        print("Bônus:{:.2f}".format(self.calculaBonus(mes, ano)))

    @abstractmethod
    def calculaSalario(self, mes, ano):
        pass

    @abstractmethod
    def calculaBonus(self, mes, ano):
        pass

class Professor(Funcionario):
    def __init__(self, codigo, nome, titulacao, salHora, nroAulas):
        super().__init__(codigo, nome)
        self.__titulacao = titulacao
        self.__salHora = salHora
        self.__nroAulas = nroAulas

    def getTitulacao(self):
        return self.__titulacao

    def getSalHora(self):
        return self.__salHora

    def getNroAulas(self):
        return self.__nroAulas

    def calculaSalario(self, mes, ano):
        pMensal = None
        for folha in self.getPontoMensal():
            if (folha.getMes() == mes and folha.getAno() == ano):
                pMensal = folha
                break
        salarioProf = self.__salHora * self.__nroAulas - self.__salHora  * pMensal.getNroFaltas()
        return salarioProf

    def calculaBonus(self, mes, ano):
        pMensal = None
        for folha in self.getPontoMensal():
            if (folha.getMes() == mes and folha.getAno() == ano):
                pMensal = folha
                break
        if(pMensal.getNroAtrasos() < 10):
            return (self.calculaSalario(mes, ano) * (10 - pMensal.getNroAtrasos())) / 100
        return 0

class TecAdmin(Funcionario):
    def __init__(self, codigo, nome, funcao, salMensal):
        super().__init__(codigo, nome)
        self.__funcao = funcao
        self.__salMensal = salMensal

    def getFuncao(self):
        return self.__funcao

    def getSalMensal(self):
        return self.__salMensal

    def calculaSalario(self, mes, ano):
        pMensal = None
        for folha in self.getPontoMensal():
            if (folha.getMes() == mes and folha.getAno() == ano):
                pMensal = folha
        salarioTec = self.getSalMensal() - (self.getSalMensal()/30) * pMensal.getNroFaltas()
        return salarioTec

    def calculaBonus(self, mes, ano):
        pMensal = None
        for folha in self.getPontoMensal():
            if (folha.getMes() == mes and folha.getAno() == ano):
                pMensal = folha
                break
        if(pMensal.getNroAtrasos() < 8):
            return (self.calculaSalario(mes, ano) * (8 - pMensal.getNroAtrasos()))/ 100
        return 0

if __name__ == "__main__":
    funcionarios = []
    prof = Professor(1, "Joao", "Doutor", 45.35, 32)   
    prof.adicionaPonto(4, 2021, 0, 0)
    prof.lancaFaltas(4, 2021, 2)
    prof.lancaAtrasos(4, 2021, 3)
    funcionarios.append(prof)
    tec = TecAdmin(2, "Pedro", "Analista Contábil", 3600)
    tec.adicionaPonto(4, 2021, 0, 0)
    tec.lancaFaltas(4, 2021, 3)
    tec.lancaAtrasos(4, 2021, 4)
    funcionarios.append(tec)
    for func in funcionarios:
        func.imprimeFolha(4, 2021)
        print()