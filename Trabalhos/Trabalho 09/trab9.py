from abc import ABC

class TitulacaoInvalida(Exception):
    pass

class IdadeInvalida(Exception):
    pass

class CursoInvalido(Exception):
    pass

class CpfRepitido(Exception):
    pass

class Pessoa(ABC):
    def __init__(self, nome, cpf, endereco, idade):
        self.nome = nome
        self.cpf = cpf
        self.endereco = endereco
        self.idade = idade
        
    def getNome(self):
        return self.nome
    def getCpf(self):
        return self.cpf
    def getEndereco(self):
        return self.endereco
    def getIdade(self):
        return self.idade
    def printDescricao(self):
        print("Nome: ", self.nome)
        print("CPF: ", self.cpf)
        print("Endereco: ", self.endereco)
        print("Idade: ", self.idade)
        
class Professor(Pessoa):
    def __init__(self, nome, cpf, endereco, idade, titulacao):
        super().__init__(nome, cpf, endereco, idade)
        self.titulacao = titulacao
    def getTitulacao(self):
        return self.titulacao
    def printDescricao(self):
        super().printDescricao()
        print("Titulação: ", self.titulacao)
        
class Aluno(Pessoa):
    def __init__(self, nome, cpf, endereco, idade, curso):
        super().__init__(nome, cpf, endereco, idade)
        self.curso = curso
    def getCurso(self):
        return self.curso
    def printDescricao(self):
        super().printDescricao()
        print("Curso: ", self.curso)
        
if __name__ == "__main__":
    lista = [
        Professor("Paulo", "123.456.789-00", "Rua A", 44, "Doutor"),
        Professor("Maria", "243.445.333-02", "Rua B", 33, "Mestre"),
        Professor("Paulo", "123.456.789-00", "Rua A", 44, "Doutor"),
        Professor("Marcos", "324.879.456-03", "Rua D", 15, "Doutor"),        
        Aluno("Pedro", "234.436.234-44", "Rua D", 19, "SIN"),
        Aluno("Marisa", "574.326.456-33", "Rua E", 23, "CCO"),
        Aluno("Marta", "867.345.456-34", "Rua F", 22, "ECO"),
        Aluno("Pedro", "234.436.234-44", "Rua D", 19, "SIN"),
        Aluno("Ana", "344.336.359-20", "Rua G", -22, "SIN"),
        Aluno("Paulo", "123.456.789-00", "Rua A", 44, "SIN"),
    ]
    
    cadastro = {}
    
    for pessoa in lista:
        try:
            if pessoa.getCpf() in cadastro:
                raise CpfRepitido()
            if type(pessoa) == Professor:
                if pessoa.getTitulacao() not in ["Doutor"]:
                    raise TitulacaoInvalida()
                if pessoa.getIdade() < 30:
                    raise IdadeInvalida()
            else:
                if pessoa.getCurso() not in ["SIN", "CCO"]:
                    raise CursoInvalido()
                if pessoa.getIdade() < 18:
                    raise IdadeInvalida()
        except (CpfRepitido):
            print("Erro: CPF repetido: ", pessoa.getNome())
        except (TitulacaoInvalida):
            print("Erro: Titulação inválida: " + pessoa.getNome())
        except (CursoInvalido):
            print("Erro: Curso inválido: " + pessoa.getNome())
        except (IdadeInvalida):
            print("Erro: Idade inválida: " + pessoa.getNome())
        else:
            cadastro[pessoa.getCpf()] = pessoa
            print("Cadastro realizado com sucesso!")
            pessoa.printDescricao()
        finally:
            print()