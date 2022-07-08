import tkinter as tk
from tkinter import messagebox, simpledialog
from tkinter import ttk

class DisciplinaCursada:
    def __init__(self, disciplina, ano, semestre, nota):
        self.__disciplina = disciplina
        self.__ano = ano
        self.__semestre = semestre
        self.__nota = nota
        
    def getDisciplina(self):
        return self.__disciplina
    
    def getSemestre(self):
        return self.__semestre
    
    def getNota(self):
        return self.__nota
    
    def getAno(self):
        return self.__ano

class Historico:
    def __init__(self):
        self.__historico = []
        
    def addMateria(self, disciplina, ano, semestre, nota):
        disciplinaCursada = DisciplinaCursada(disciplina, ano, semestre, nota)
        self.__historico.append(disciplinaCursada)
    
    def getHistorico(self):
        return self.__historico
    
    def getDisciplinas(self):
        disciplinas = []
        for disciplinaCursada in self.__historico:
            disciplinas.append(disciplinaCursada.getDisciplina())
        return disciplinas

class Aluno:
    def __init__(self, nroMatricula, nome, curso):
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
        return self.__historico
        
    def addDisciplina(self, disciplina):
        self.__historico.addMateria(disciplina)
        
    def getCargaHoraria(self):
        cargaHorariaObrigatoria = 0
        carregaHorariaEletiva = 0
        for disciplina in self.__historico.getDisciplinas():
            if disciplina in self.__curso.getDisciplinas():
                cargaHorariaObrigatoria += disciplina.getCargaHoraria()
            else:
                carregaHorariaEletiva += disciplina.getCargaHoraria()
            
        return [cargaHorariaObrigatoria, carregaHorariaEletiva]

class LimiteInsereAluno(tk.Toplevel):
    def __init__(self, controle, listaCursosCod):

        tk.Toplevel.__init__(self)
        self.geometry('250x100')
        self.title("Estudante")
        self.controle = controle

        self.frameNro = tk.Frame(self)
        self.frameNome = tk.Frame(self)
        self.frameCurso = tk.Frame(self)
        self.frameButton = tk.Frame(self)
        self.frameNro.pack()
        self.frameNome.pack()
        self.frameCurso.pack()
        self.frameButton.pack()
      
        self.labelNro = tk.Label(self.frameNro,text="Nro Matrícula: ")
        self.labelNome = tk.Label(self.frameNome,text="Nome: ")
        self.labelNro.pack(side="left")
        self.labelNome.pack(side="left")  

        self.inputNro = tk.Entry(self.frameNro, width=20)
        self.inputNro.pack(side="left")
        self.inputNome = tk.Entry(self.frameNome, width=20)
        self.inputNome.pack(side="left")            
        
        self.labelDiscip = tk.Label(self.frameCurso,text="Escolha o curso: ")
        self.labelDiscip.pack(side="left")
        self.escolhaCombo = tk.StringVar()
        self.combobox = ttk.Combobox(self.frameCurso, width = 15 , textvariable = self.escolhaCombo)
        self.combobox.pack(side="left")
        self.combobox['values'] = listaCursosCod
      
        self.buttonSubmit = tk.Button(self.frameButton ,text="Criar")      
        self.buttonSubmit.pack(side="left")
        self.buttonSubmit.bind("<Button>", controle.criaAluno)
      
        self.buttonClear = tk.Button(self.frameButton ,text="Clear")      
        self.buttonClear.pack(side="left")
        self.buttonClear.bind("<Button>", controle.clearHandlerIns)  

    def mostraJanela(self, titulo, msg):
        messagebox.showinfo(titulo, msg)
        

class LimiteInsereAlunoDisciplina(tk.Toplevel):
    def __init__(self, controle, listaDiscCod):

        tk.Toplevel.__init__(self)
        self.geometry('250x100')
        self.title("Estudante")
        self.controle = controle

        self.frameNota = tk.Frame(self)
        self.frameNota.pack(side="left")
        self.frameAno = tk.Frame(self)
        self.frameAno.pack(side="left")
        self.frameSemestre = tk.Frame(self)
        self.frameSemestre.pack(side="left")
        self.frameButton = tk.Frame(self)
        self.frameButton.pack(side="left")
        self.frameDiscip = tk.Frame(self)
        self.frameDiscip.pack(side="left")
      
        self.labelNota= tk.Label(self.frameNota,text="Nota:")
        self.labelAno = tk.Label(self.frameAno,text="Ano")
        self.labelSemestre = tk.Label(self.frameSemestre,text="Semestre")
        self.labelAno.pack(side="left")
        self.labelNota.pack(side="left")
        self.labelSemestre.pack(side="left")

        self.inputNota = tk.Entry(self.frameNota, width=20)
        self.inputNota.pack(side="left")
        self.inputNome = tk.Entry(self.frameAno, width=20)
        self.inputNome.pack(side="left")    
        self.inputSemestre = tk.Entry(self.frameSemestre, width=20)
        self.inputSemestre.pack(side="left")        
        
        self.labelDiscip = tk.Label(self.frameDiscip,text="Escolha o Disciplina: ")
        self.labelDiscip.pack(side="left")
        self.escolhaCombo = tk.StringVar()
        self.combobox = tk.Combobox(self.frameDiscip, width = 15 , textvariable = self.escolhaCombo)
        self.combobox.pack(side="left")
        self.combobox['values'] = listaDiscCod
      
        self.buttonSubmit = tk.Button(self.frameButton ,text="Enter")      
        self.buttonSubmit.pack(side="left")
        self.buttonSubmit.bind("<Button>", controle.insereDisciplinaHandler)
      
        self.buttonClear = tk.Button(self.frameButton ,text="Clear")      
        self.buttonClear.pack(side="left")
        self.buttonClear.bind("<Button>", controle.clearHandlerInsDisc)  

    def mostraJanela(self, titulo, msg):
        messagebox.showinfo(titulo, msg)

class LimiteMensagem():
    def __init__(self, str):
        messagebox.showinfo('Aluno', str)

class CtrlAluno():       
    def __init__(self, controlePrincipal):
        self.ctrlPrincipal = controlePrincipal
        self.listaAlunos = []

    def insereAlunos(self):        
        self.listaAlunosTurma = []
        listaCursosCod = self.ctrlPrincipal.ctrlCurso.getListaCodCursos()
        self.limiteIns = LimiteInsereAluno(self, listaCursosCod)

    def criaAluno(self, event):
        nroMatric = self.limiteIns.inputNro.get()
        nome = self.limiteIns.inputNome.get()
        cursoCod = self.limiteIns.escolhaCombo.get()
        curso = self.ctrlPrincipal.ctrlCurso.getCurso(cursoCod)
        aluno = Aluno(nroMatric, nome, curso)
        self.listaAlunos.append(aluno)
        self.limiteIns.mostraJanela('Sucesso', 'Estudante cadastrado com sucesso')
        self.clearHandlerIns(event)
        self.limiteIns.destroy()
        
    def clearHandlerIns(self, event):
        self.limiteIns.inputNro.delete(0, tk.END)
        self.limiteIns.inputNome.delete(0, tk.END)
        self.limiteIns.escolhaCombo.set('')
        
    def clearHandlerInsDisc(self, event):
        self.limiteInsDisciplina.inputNro.delete(0, tk.END)
        self.limiteInsDisciplina.inputNome.delete(0, tk.END)
        self.limiteInsDisciplina.escolhaCombo.set('')
        self.limiteInsDisciplina.inputSemestre.delete(0, tk.END)
        
    def cadastraDsciplinaCursada(self):
        matricula = simpledialog.askstring('Aluno', 'Digite o código do aluno: ')
        alunoSel = None
        for aluno in self.listaAlunos:
            if matricula == aluno.getNroMatricula():
                alunoSel = aluno
                
        if alunoSel is not None:
            self.alunoSel = alunoSel
        else:
            self.ctrlPrincipal.limite.mostraJanela('Erro', 'Aluno não encontrado')
            return
            
        disciplinas = self.ctrlPrincipal.ctrlDisciplina.getDisciplinas()
        disciplinasNCursadas= []
        disciplinasCursadas =  alunoSel.getHistorico().getDisciplinas()
        for disciplina in disciplinas:
            if disciplina not in disciplinasCursadas:
                disciplinasNCursadas.append(disciplina)
                
        disciplinasCod = []        
        for disciplina in disciplinasNCursadas:
            disciplinasCod.append(disciplina.getCodigo())
                
        self.limiteInsDisciplina = LimiteInsereAlunoDisciplina(self, disciplinasCod)
       
    def insereDisciplinaHandler(self, event):   
            disciplinaCod = self.limiteInsDisciplina.escolhaCombo.get()
            disciplina = self.ctrlPrincipal.ctrlDisciplina.getDisciplina(disciplinaCod)
            ano = self.limiteInsDisciplina.inputAno.get()
            semestre = self.limiteInsDisciplina.inputSemestre.get()
            nota = self.limiteInsDisciplina.inputNota.get()
            self.alunoSel.getHistorico().addDisciplina(disciplina, ano, semestre, nota)
            self.limiteInsDisciplina.mostraJanela('Sucesso', 'Disciplina cadastrada com sucesso')
            self.clearHandlerInsDisc(event)
            self.limiteInsDisciplina.destroy()
            
    def consultarAluno(self):
        alunoCod = simpledialog.askstring('Aluno', 'Digite o código do aluno: ')
        aluno = None
        for el in self.listaAlunos:
            if alunoCod == el.getNroMatricula():
                aluno = el
                
        if aluno is not None:
            res = 'Nome: ' + aluno.getNome() + '\n'
            res += 'Matrícula: ' + aluno.getNroMatricula() + '\n'
            res += 'Curso: ' + aluno.getCurso().getNome() + '\n'
            obrigatoria, pendente = aluno.getCargaHoraria()
            res += 'Carga horária obrigatória: ' + str(obrigatoria) + '\n'
            res += 'Carga horária pendente: ' + str(pendente) + '\n'
            for disciplinaCursada in aluno.getHistorico().getDisciplinas():
                disciplina = disciplinaCursada.getDisciplina()
                res += '---------------------'
                res += 'Disciplina: ' + disciplina.getNome() + '\n'
                res += 'Código: ' + disciplina.getCodigo() + '\n'
                res += 'Semestre: ' + str(disciplinaCursada.getSemestre()) + '\n'
                res += 'Nota: ' + str(disciplinaCursada.getNota()) + '\n'
                res += 'Ano: ' + str(disciplinaCursada.getAno()) + '\n'
                res += '---------------------'
            self.ctrlPrincipal.limite.mostraJanela('Aluno', res)
        else:
            self.ctrlPrincipal.limite.mostraJanela('Erro', 'Aluno não encontrado')