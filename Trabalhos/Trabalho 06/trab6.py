 
class Historico:
    def __init__(self):
        self.__historico = []
        
    def addMateria(self, disciplina):
        self.__historico.append(disciplina)
    
    def getHistorico(self):
        return self.__historico

class Aluno:
    def __init__(self, nome, nroMatricula, curso):
        self.__nome = nome
        self.__nroMatricula = nroMatricula
        self.__curso = curso
        self.__historico = Historico()
        
    def getNome(self):
        return self.__nome
    
    def getNroMatricula(self):
        return self.__nroMatricula
    
    def getCurso(self):
        return self.__curso
    
    def getHistorico(self):
        return self.__historico.getHistorico()
        
    def addDisciplina(self, disciplina):
        self.__historico.addMateria(disciplina)
        
    def getCargaHoraria(self):
        cargaHorariaObrigatoria = 0
        carregaHorariaEletiva = 0
        for disciplina in self.__historico.getHistorico():
            if disciplina in self.__curso.getDisciplinas():
                cargaHorariaObrigatoria += disciplina.getCargaHoraria()
            else:
                carregaHorariaEletiva += disciplina.getCargaHoraria()
            
        return [cargaHorariaObrigatoria, carregaHorariaEletiva]
    
    def printInfos(self):
        chObrigatoria, chEletiva = self.getCargaHoraria()
        
        print()
        print("Nome: " + self.__nome)
        print("Nro Matricula: " + self.__nroMatricula)
        print("Curso: " + self.__curso.getNome())
        print("Materias Cursadas: " + str(len(self.__historico.getHistorico())))
        print("Carga Horaria Obrigatoria: " + str(chObrigatoria))
        print("Carga Horaria Eletiva: " + str(chEletiva))
        print("Carga Horaria Total: " + str(chObrigatoria + chEletiva))
    
    
class Disciplina:
    def __init__(self, codigo, nome, cargaHoraria):
        self.__codigo = codigo
        self.__nome = nome
        self.__cargaHoraria = cargaHoraria
        
    def getCodigo(self):
        return self.__codigo
    
    def getNome(self):
        return self.__nome
    
    def getCargaHoraria(self):
        return self.__cargaHoraria
    
class Grade:
    def __init__(self, ano):
        self.__ano = ano
        self.__disciplinas = []
        
    def getAno(self):
        return self.__ano
        
    def addDisciplina(self, disciplina):
        self.__disciplinas.append(disciplina)
    
    def getDisciplinas(self):
        return self.__disciplinas
        
    
class Curso:
    def __init__(self, nome, grade):
        self.__nome = nome
        self.__grade = grade

    def getNome(self):
        return self.__nome
    
    def getGrade(self):
        return self.__grade
    
    def getDisciplinas(self):
        return self.__grade.getDisciplinas()
        
if __name__ == "__main__":
    grade1 = Grade(2019)
    disciplina1 = Disciplina("COM110", "Introdução a Programação", 80)
    disciplina2 = Disciplina("COM111", "Programação Orientada a Objetos", 80)
    disciplina3 = Disciplina("COM112", "Programação Web", 80)
    grade1.addDisciplina(disciplina1)
    grade1.addDisciplina(disciplina2)
    grade1.addDisciplina(disciplina3)
    curso1 = Curso("Sistemas de Informação", grade1)
    
    grade2 = Grade(2019)
    disciplina4 = Disciplina("MAT101", "Matemática I", 40)
    disciplina5 = Disciplina("MAT102", "Matemática II", 40)
    disciplina6 = Disciplina("MAT103", "Matemática III", 40)
    grade2.addDisciplina(disciplina1)
    grade2.addDisciplina(disciplina4)
    grade2.addDisciplina(disciplina5)
    grade2.addDisciplina(disciplina6)
    curso2 = Curso("Matemática", grade2)

    
    aluno1 = Aluno("João", "12345", curso1)
    aluno2 = Aluno("Maria", "54321", curso2)
    
    aluno1.addDisciplina(disciplina1)
    aluno1.addDisciplina(disciplina2)
    aluno1.addDisciplina(disciplina4)
    aluno1.printInfos()
    
    aluno2.addDisciplina(disciplina1)
    aluno2.addDisciplina(disciplina3)
    aluno2.addDisciplina(disciplina4)
    aluno2.addDisciplina(disciplina5)
    aluno2.addDisciplina(disciplina6)
    aluno2.printInfos()
    