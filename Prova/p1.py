from abc import ABC, abstractmethod

from soupsieve import select

class Dependente:
    def __init__(self, nome, idade):
        self.__nome = nome
        self.__idade = idade

    def getNome(self):
        return self.__nome

    def getIdade(self):
        return self.__idade

class Diaria:
    def __init__(self, dia, mes, ano, refeicao, atraso):
        self.__dia = dia
        self.__mes = mes
        self.__ano = ano
        self.__refeicao = refeicao
        self.__atraso = atraso

    def getDia(self):
        return self.__dia

    def getMes(self):
        return self.__mes
    
    def getAno(self):
        return self.__ano

    def isRefeicao(self):
        return self.__refeicao

    def isAtraso(self):
        return self.__atraso

class Trabalhador(ABC):
    def __init__(self, cpf, nome):
        self.__cpf = cpf
        self.__nome = nome
        self.__listaDependentes = []

    def getCPF(self):
        return self.__cpf

    def getNome(self):
        return self.__nome

    def getListaDependentes(self):
        return self.__listaDependentes
    
    def insereDependente(self, nome, idade):
        dependente = Dependente(nome, idade)

        self.__listaDependentes.append(dependente)

    @abstractmethod
    def calculaPagto(self, mes, ano):
        pass

    def imprimeRecibo(self, mes, ano):
        pagamento = self.calculaPagto(mes, ano)

        print(f"Nome: {self.__nome}")
        print("Valor recebido: {:.1f}".format(pagamento))

class Empreito:
    def __init__(self, mes, ano, descricao, valor, atrasoEntrega):
        self.__mes = mes
        self.__descricao = descricao
        self.__ano = ano
        self.__valor = valor
        self.__atrasoEntrega = atrasoEntrega

    def getMes(self):
        return self.__mes
    
    def getAno(self):
        return self.__ano

    def getDescricao(self):
        return self.__descricao

    def getValor(self):
        return self.__valor

    def isAtrasoEntrega(self):
        return self.__atrasoEntrega
    

class Diarista(Trabalhador):
    def __init__(self, cpf, nome, valorDiaria):
        super().__init__(cpf, nome)
        self.__valorDiaria = valorDiaria
        self.__listaDiaria = []
    
    def getValorDiaria(self):
        return self.__valorDiaria

    def getListaDiaria(self):
        return self.__listaDiaria

    def adicionaDiaria(self, dia, mes, ano, refeicao, atraso):
        diaria = Diaria(dia, mes, ano, refeicao, atraso)
        self.__listaDiaria.append(diaria)

    def obtemValorAuxilio(self):
        if len(self.getListaDependentes()) == 0:
            return 0

        dependentesMenores = []

        for dependente in self.getListaDependentes():
            if dependente.getIdade() < 6:
                dependentesMenores.append(dependente)

        return len(dependentesMenores) * 100
    
    def calculaPagto(self, mes, ano):
        salario = 0
        auxilio = self.obtemValorAuxilio()
        trabalhou = False

        for diaria in self.getListaDiaria():
            if diaria.getMes() is mes and  diaria.getAno() is ano:
                trabalhou = True
                if diaria.isAtraso():
                    salario+= self.getValorDiaria() * 0.90
                else:
                    salario+= self.getValorDiaria()
                
                if diaria.isRefeicao():
                    salario = salario - 10

        if trabalhou is False:
            auxilio = 0

        return salario + auxilio

class Empreiteiro(Trabalhador):
    def __init__(self, cpf, nome):
        super().__init__(cpf, nome)
        self.__listaEmpreito = []

    def getListaEmpreito(self):
        return self.__listaEmpreito

    def adicionaEmpreito(self, mes, ano, descricao, valor, atrasoEntrega):
        empreito = Empreito(mes, ano, descricao, valor, atrasoEntrega)

        self.__listaEmpreito.append(empreito)

    def calculaPagto(self, mes, ano):
        salario = 0
        for empreito in self.getListaEmpreito():
            if empreito.getMes() is mes and empreito.getAno() is ano:
                if empreito.isAtrasoEntrega():
                    salario+= empreito.getValor() * 0.80
                else:
                    salario+= empreito.getValor()

        return salario
    

if __name__ == "__main__":
    listaTrab = []
    d1 = Diarista("111222", "Joao Silva", 100)
    d1.insereDependente("Pedro Silva", 4)
    d1.insereDependente("Ana Silva", 2)
    d1.adicionaDiaria(10, 3, 2022, False, False)
    d1.adicionaDiaria(12, 4, 2022, False, True)
    d2 = Diarista("222333", "Jose Cruz", 120)
    d2.insereDependente("Paula Cruz", 3)
    d2.insereDependente("Mario Cruz", 10)
    d2.adicionaDiaria(5, 4, 2022, False, False)
    d2.adicionaDiaria(6, 4, 2022, True, False)
    d2.adicionaDiaria(7, 4, 2022, True, True)
    e1 = Empreiteiro("333444", "Marcio Souza")
    e1.adicionaEmpreito(3, 2022, "Fundações", 6000, False)
    e1.adicionaEmpreito(4, 2022, "Construção muros", 4000, False)
    e1.adicionaEmpreito(4, 2022, "Instalação dos pisos", 7000, True)
    listaTrab.append(d1)
    listaTrab.append(d2)
    listaTrab.append(e1)
    for trab in listaTrab:
        trab.imprimeRecibo(4, 2022)