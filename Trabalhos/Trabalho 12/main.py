import tkinter as tk
from tkinter import messagebox
import aluno as al
import curso as cr
import disciplina as ds

class LimitePrincipal():
    def __init__(self, root, controle):
        self.controle = controle
        self.root = root
        self.root.geometry('300x250')
        self.menubar = tk.Menu(self.root)        
        self.alunoMenu = tk.Menu(self.menubar)
        self.cursoMenu = tk.Menu(self.menubar)
        self.disciplinaMenu = tk.Menu(self.menubar)
        self.sairMenu = tk.Menu(self.menubar)    

        self.alunoMenu.add_command(label="Criar", \
                    command=self.controle.insereAlunos)
        self.alunoMenu.add_command(label="Cadastrar Disciplina Cursada", \
                    command=self.controle.cadastraDsciplinaCursada)
        self.alunoMenu.add_command(label="Consultar", \
            command=self.controle.consultarAluno)
        self.menubar.add_cascade(label="Aluno", \
                    menu=self.alunoMenu)

        self.cursoMenu.add_command(label="Criar", \
                    command=self.controle.insereCurso)
        self.cursoMenu.add_command(label="Consultar", \
                    command=self.controle.consultarCurso)        
        self.menubar.add_cascade(label="Curso", \
                    menu=self.cursoMenu)

        self.disciplinaMenu.add_command(label="Insere", \
                    command=self.controle.insereDisciplina)                   
        self.menubar.add_cascade(label="Disciplina", \
                    menu=self.disciplinaMenu)        

        self.sairMenu.add_command(label="Salva", \
                    command=self.controle.salvaDados)
        self.menubar.add_cascade(label="Sair", \
                    menu=self.sairMenu)

        self.root.config(menu=self.menubar)
    
    def mostraJanela(self, titulo, msg):
        messagebox.showinfo(titulo, msg)

      
class ControlePrincipal():       
    def __init__(self):
        self.root = tk.Tk()

        self.ctrlAluno = al.CtrlAluno(self)
        self.ctrlDisciplina = ds.CtrlDisciplina(self)
        self.ctrlCurso = cr.CtrlCurso(self)

        self.limite = LimitePrincipal(self.root, self) 

        self.root.title("Trab 12")
        # Inicia o mainloop
        self.root.mainloop()
       
    def insereAlunos(self):
        self.ctrlAluno.insereAlunos()

    def cadastraDsciplinaCursada(self):
        self.ctrlAluno.cadastraDsciplinaCursada()
        
    def consultarAluno(self):
        self.ctrlAluno.consultarAluno()

    def insereCurso(self):
        self.ctrlCurso.insereCurso()
        
    def consultarCurso(self):
        self.ctrlCurso.consultarCurso()

    def insereDisciplina(self):
        self.ctrlDisciplina.insereDisciplina()

    def salvaDados(self):
        self.ctrlAluno.salvaDados()
        self.ctrlCurso.salvaDados()
        self.ctrlDisciplina.salvaDados()
        self.root.destroy()

if __name__ == '__main__':
    c = ControlePrincipal()