import tkinter as tk
from tkinter import messagebox
from tkinter import ttk
 
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
    
class LimiteInsereDisciplina(tk.Toplevel):
    def __init__(self, controle, listGradesOption):

        tk.Toplevel.__init__(self)
        self.geometry('250x200')
        self.title("Disciplina")
        self.controle = controle

        self.frameNome = tk.Frame(self)
        self.frameNome.pack()
        self.frameCod = tk.Frame(self)
        self.frameCod.pack()
        self.frameHoras = tk.Frame(self)
        self.frameHoras.pack()
        self.frameGrade = tk.Frame(self)
        self.frameGrade.pack()
        self.frameButton = tk.Frame(self)
        self.frameButton.pack()
      
        self.labelNome= tk.Label(self.frameNome,text="Nome:")
        self.labelNome.pack(side="left")  
        
        self.labelCod= tk.Label(self.frameCod,text="Codigo:")
        self.labelCod.pack(side="left")
        
        self.labelHoras= tk.Label(self.frameHoras,text="Carga Horaria:")
        self.labelHoras.pack(side="left")

        self.inputNome = tk.Entry(self.frameNome, width=20)
        self.inputNome.pack(side="left")    
        
        self.inputCod = tk.Entry(self.frameCod, width=20)
        self.inputCod.pack(side="left")
      
        self.inputHoras = tk.Entry(self.frameHoras, width=20)
        self.inputHoras.pack(side="left") 
        
        self.labelGrade = tk.Label(self.frameGrade,text="Escolha a grade: ")
        self.labelGrade.pack(side="left")
        self.escolhaCombo = tk.StringVar()
        self.combobox = ttk.Combobox(self.frameGrade, width = 15 , textvariable = self.escolhaCombo)
        self.combobox.pack(side="left")
        self.combobox['values'] = listGradesOption
            
        self.buttonSubmit = tk.Button(self.frameButton ,text="Criar Disciplina")      
        self.buttonSubmit.pack(side="left")
        self.buttonSubmit.bind("<Button>", controle.criarDisciplina)
      
        self.buttonClear = tk.Button(self.frameButton ,text="Clear")      
        self.buttonClear.pack(side="left")
        self.buttonClear.bind("<Button>", controle.clearHandler)  

    def mostraJanela(self, titulo, msg):
        messagebox.showinfo(titulo, msg)
        
class LimiteMensagem():
    def __init__(self, str):
        messagebox.showinfo('Aluno', str)

class CtrlDisciplina():       
    def __init__(self, controlePrincipal):
        self.ctrlPrincipal = controlePrincipal
        self.listaCursos = []
        self.listaDisciplinas = []

    def insereDisciplina(self):        
        listGradesOption = self.ctrlPrincipal.ctrlCurso.getListaCodGrades()
        self.limiteIns = LimiteInsereDisciplina(self, listGradesOption)

    def criarDisciplina(self, event):
        nome = self.limiteIns.inputNome.get()
        cod = self.limiteIns.inputCod.get()
        horas = self.limiteIns.inputHoras.get()
        gradeSel = self.limiteIns.escolhaCombo.get()
        disciplina = Disciplina(cod, nome, horas)
        self.ctrlPrincipal.ctrlCurso.addMateriaGrade(disciplina, gradeSel)
        self.listaDisciplinas.append(disciplina)
        self.limiteIns.mostraJanela("Disciplina", "Disciplina criada com sucesso!")
        self.limiteIns.destroy()
    
    def getDisciplinas(self):
        return self.listaDisciplinas
    
    def getDisciplina(self, codigo):
        for d in self.listaDisciplinas:
            if d.getCodigo() == codigo:
                return d
        return None
    
    def getListaCodDisciplinas(self):
        listaCodDisciplinas = []
        for d in self.listaDisciplinas:
            listaCodDisciplinas.append(d.getCodigo())
        return listaCodDisciplinas
    
    def clearHandler(self, event):
        self.limiteIns.inputNome.delete(0, tk.END)
        self.limiteIns.inputCod.delete(0, tk.END)
        self.limiteIns.inputHoras.delete(0, tk.END)