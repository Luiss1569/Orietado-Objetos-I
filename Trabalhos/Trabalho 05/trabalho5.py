from abc import ABC, abstractmethod

class EmpDomestica(ABC):
    def __init__(self, nome, telefone):
        self.nome = nome
        self.telefone = telefone

    def get_nome(self):
        return self.nome
    
    def set_nome(self, nome):
        self.nome = nome
        
    def get_telefone(self):
        return self.telefone
    
    def set_telefone(self, telefone):
        self.telefone = telefone
        
    @abstractmethod
    def get_salario(self):
        pass
    
    
class Horista(EmpDomestica):
    def __init__(self, nome, telefone, horas_trabalhadas, valor_hora):
        super().__init__(nome, telefone)
        self.horas_trabalhadas = horas_trabalhadas
        self.valor_hora = valor_hora
        
    def get_salario(self):
        return self.horas_trabalhadas * self.valor_hora
    
class Diarista(EmpDomestica):
    def __init__(self, nome, telefone, dias_trabalhados, valor_dia):
        super().__init__(nome, telefone)
        self.dias_trabalhados = dias_trabalhados
        self.valor_dia = valor_dia
        
    def get_salario(self):
        return self.dias_trabalhados * self.valor_dia
    
class Mensalista(EmpDomestica):
    def __init__(self, nome, telefone, valor_mes):
        super().__init__(nome, telefone)
        self.valor_mes = valor_mes
        
    def get_salario(self):
        return self.valor_mes

if __name__ == "__main__":
    holista = Horista("Ana", "9999-9999", 160, 10)
    diarista = Diarista("Paula", "8888-8888", 20, 55)
    mensalista = Mensalista("Marcia", "7777-7777", 1000)
    
    emps = [holista, diarista, mensalista]
    
    menor = emps[0]
    for emp in emps:
        print(f"{emp.get_nome()} - {emp.get_telefone()} - {emp.get_salario()} reais por mês")
        if emp.get_salario() < menor.get_salario():
            menor = emp
    
    print(f"\nO menor salário é da {menor.get_nome()} de {menor.get_salario()} reais")
    