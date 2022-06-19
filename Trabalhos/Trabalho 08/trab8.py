from abc import ABC, abstractmethod
from datetime import date

class Transacao(ABC):
    def __init__(self, valor, data):
        self.__valor = valor
        self.__data = data
        
    def getValor(self):
        return self.__valor
    
    def getData(self):
        return self.__data
    
class Saque(Transacao):
    def __init__(self, valor, data, senha):
        super().__init__(valor * -1, data)
        self.__senha = senha
    
    def getSenha(self):
        return self.__senha
    
class Deposito(Transacao):
    def __init__(self, valor, data, nomeDepositante):
        super().__init__(valor, data)
        self.__nomeDepositante = nomeDepositante
        
    def getNomeDepositante(self):
        return self.__nomeDepositante
    
class Transferencia(Transacao):
    def __init__(self, valor, data, senha, tipoTrans):
        super().__init__(valor if tipoTrans == 'C' else valor * -1, data)
        self.__senha = senha
        self.__tipoTrans = tipoTrans
    
    def getSenha(self):
        return self.__senha
    
    def getTipoTrans(self):
        return self.__tipoTrans

class Conta:
    def __init__(self, nroConta,nome, limite, senha):
        self.__nroConta = nroConta
        self.__nome = nome
        self.__limite = limite
        self.__senha = senha
        self.__transacoes = []
        
    def getNroConta(self):
        return self.__nroConta
    
    def getNome(self):
        return self.__nome
    
    def getLimite(self):
        return self.__limite
    
    def getSenha(self):
        return self.__senha
    
    def getTransacoes(self):
        return self.__transacoes
    
    def adicionaDeposito(self, valor, data, nomeDepositante):
        self.__transacoes.append(Deposito(valor, data, nomeDepositante))
        
    def adicionaSaque(self, valor, data, senha):
        if senha is not self.__senha:
            return False
        if valor > self.calculaSaldo(): 
            return False
        
        self.__transacoes.append(Saque(valor, data, senha))
        
    def adicionaTransf(self, valor, data, senha, contaFavorecido):
        if contaFavorecido is None:
            self.__transacoes.append(Transferencia(valor, data, senha, 'C'))
            return True
        
        if senha is not self.__senha:
            return False
        if valor > self.calculaSaldo(): 
            return False

        self.__transacoes.append(Transferencia(valor, data, senha, "D"))
        contaFavorecido.adicionaTransf(valor, data, '', None)
        
    def calculaSaldo(self):
        saldo = 0
        for transacao in self.__transacoes:
            saldo += transacao.getValor()
        return saldo + self.__limite
    

if __name__ == "__main__":
    c1 = Conta(1234, 'Jose da Silva', 1000, 'senha1')     
    c1.adicionaDeposito(5000, date.today(), 'Antonio Maia')     
    if c1.adicionaSaque(2000, date.today(), 'senha1') == False:         
        print('Não foi possível realizar o saque no valor de 2000')     
    if c1.adicionaSaque(1000, date.today(), 'senha-errada') == False: # deve falhar         
        print('Não foi possível realizar o saque no valor de 1000')
             
    c2 = Conta(4321, 'Joao Souza', 1000, 'senha2')     
    c2.adicionaDeposito(3000, date.today(), 'Maria da Cruz')     
    if c2.adicionaSaque(1500, date.today(), 'senha2') == False:         
        print('Não foi possível realizar o saque no valor de 1500')     
    if c2.adicionaTransf(5000, date.today(), 'senha2', c1) == False:  # deve falhar         
        print('Não foi possível realizar a transf no valor de 5000')     
    if c2.adicionaTransf(800, date.today(), 'senha2', c1) == False:         
        print('Não foi possível realizar a transf no valor de 800')
        
    print('--------')     
    print('Saldo de c1: {}'.format(c1.calculaSaldo()))  # deve imprimir 4800     
    print('Saldo de c2: {}'.format(c2.calculaSaldo()))  # deve imprimir 1700 