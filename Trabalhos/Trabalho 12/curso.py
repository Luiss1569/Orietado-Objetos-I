import tkinter as tk
from tkinter import messagebox, simpledialog
import pickle
import os.path

class Grade:
    def __init__(self, ano, disciplinas):
        self.__ano = ano
        self.__disciplinas = disciplinas
        
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
    
    def eObrigatoria(self, disciplina):
        for d in self.__grade.getDisciplinas():
            if d.getCodigo() == disciplina.getCodigo():
                return True
        return False

class LimiteInsereCurso(tk.Toplevel):
    def __init__(self, controle, listaDisciplinasCod):

        tk.Toplevel.__init__(self)
        self.geometry('250x400')
        self.title("Curso")
        self.controle = controle

        self.frameNome = tk.Frame(self)
        self.frameAno = tk.Frame(self)
        self.frameGrade = tk.Frame(self)
        self.frameButton = tk.Frame(self)
        self.frameNome.pack()
        self.frameAno.pack()
        self.frameGrade.pack()
        self.frameGrade.pack()
        self.frameButton.pack()
      
        self.labelNome= tk.Label(self.frameNome,text="Nome:")
        self.labelNome.pack()  
        
        self.labelAno= tk.Label(self.frameAno,text="Ano da grade:")
        self.labelAno.pack()

        self.inputNome = tk.Entry(self.frameNome, width=20)
        self.inputNome.pack(side="left")         
        
        self.inputAno = tk.Entry(self.frameAno, width=20)
        self.inputAno.pack(side="left")
        
        self.labelEst = tk.Label(self.frameGrade,text="Escolha as materias: ")
        self.labelEst.pack() 
        
        self.listbox = tk.Listbox(self.frameGrade)
        self.listbox.pack()
        for nro in listaDisciplinasCod:
            self.listbox.insert(tk.END, nro)
      
        self.buttonSubmit = tk.Button(self.frameButton ,text="Criar Curso")      
        self.buttonSubmit.pack(side="left")
        self.buttonSubmit.bind("<Button>", controle.criaCurso)
        
        self.buttonSubmitDisc = tk.Button(self.frameButton ,text="Add disciplina")      
        self.buttonSubmitDisc.pack(side="left")
        self.buttonSubmitDisc.bind("<Button>", controle.insereDisciplinas)
      
        self.buttonClear = tk.Button(self.frameButton ,text="Clear")      
        self.buttonClear.pack(side="left")
        self.buttonClear.bind("<Button>", controle.clearHandler)  

        self.buttonFecha = tk.Button(self.frameButton ,text="Concluído")      
        self.buttonFecha.pack(side="left")
        self.buttonFecha.bind("<Button>", controle.closeHandler)

    def mostraJanela(self, titulo, msg):
        messagebox.showinfo(titulo, msg)
        


class LimiteMensagem():
    def __init__(self, str):
        messagebox.showinfo('Aluno', str)

class CtrlCurso():       
    def __init__(self, controlePrincipal):
        self.ctrlPrincipal = controlePrincipal
        self.listaDisciplinas = []
        if not os.path.isfile("cursos.pickle"):
            self.listaCursos =  []
        else:
            with open("cursos.pickle", "rb") as f:
                self.listaCursos = pickle.load(f)
                
    def salvaDados(self):
        if len(self.listaCursos) != 0:
            with open("cursos.pickle","wb") as f:
                pickle.dump(self.listaCursos, f)
        
    def closeHandler(self, event):
        self.limiteIns.destroy()

    def insereCurso(self):        
        self.listaDisciplinas = []
        listaDiscCod = self.ctrlPrincipal.ctrlDisciplina.getListaCodDisciplinas()
        self.limiteIns = LimiteInsereCurso(self, listaDiscCod)
        
    def insereDisciplinas(self, event):
        disciplinaSel = self.limiteIns.listbox.get(tk.ACTIVE)
        disciplina = self.ctrlPrincipal.ctrlDisciplina.getDisciplina(disciplinaSel)
        self.listaDisciplinas.append(disciplina)
        self.limiteIns.mostraJanela('Sucesso', 'Disciplina cadastrada com sucesso')
        self.limiteIns.listbox.delete(tk.ACTIVE)
        
    def consultarCurso(self):
        cursoCod = simpledialog.askstring("Consultar Curso", "Digite o código do curso:")
        curso = self.getCurso(cursoCod)
        str = ""
        
        if curso == None:
            str = "Curso não encontrado"
        else:
            str = "Nome: " + curso.getNome() + "\n"
            str += "Ano: " + curso.getGrade().getAno() + "\n"
            str += "Disciplinas: " + "\n"
            for disc in curso.getGrade().getDisciplinas():
                str += disc.getCodigo() + " - " + disc.getNome() + "\n"
        
        self.ctrlPrincipal.limite.mostraJanela("Curso", str)

    def criaCurso(self, event):
        nome = self.limiteIns.inputNome.get()
        ano = self.limiteIns.inputAno.get()
        grade = Grade(ano, self.listaDisciplinas)
        curso = Curso(nome, grade)
        self.listaCursos.append(curso)
        self.limiteIns.mostraJanela('Sucesso', 'Estudante cadastrado com sucesso')
        self.limiteIns.destroy()
    
    def getListaCodCursos(self):
        listaCod = []
        for curso in self.listaCursos:
            listaCod.append(curso.getNome())
        return listaCod
    
    def getCurso(self, nome):
        for curso in self.listaCursos:
            if curso.getNome() == nome:
                return curso
        return None
    
    def clearHandler(self, event):
        self.limiteIns.inputNome.delete(0, tk.END)
        self.limiteIns.inputAno.delete(0, tk.END)
        
    def getListaCodGrades(self):
        listaCod = []
        for curso in self.listaCursos:
            listaCod.append(curso.getGrade().getAno())
        return listaCod
    
    def addMateriaGrade(self, materia, gradeSel):
        for curso in self.listaCursos:
            if curso.getGrade().getAno() == gradeSel:
                curso.getGrade().addDisciplina(materia)
                break