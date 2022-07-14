import tkinter as tk
from tkinter import messagebox
import produto as pr
import cupom as cu

class LimitePrincipal():
    def __init__(self, root, controle):
        self.controle = controle
        self.root = root
        self.root.geometry('300x250')
        self.menubar = tk.Menu(self.root)        
        self.produtoMenu = tk.Menu(self.menubar)
        self.cupomMenu = tk.Menu(self.menubar)
        self.playlistMenu = tk.Menu(self.menubar)
        self.sairMenu = tk.Menu(self.menubar)    

        self.produtoMenu.add_command(label="Cadastrar", \
                    command=self.controle.insereProduto)
        self.produtoMenu.add_command(label="Consultar", \
            command=self.controle.consultaProduto)
        self.menubar.add_cascade(label="Produto", \
                    menu=self.produtoMenu)

        self.cupomMenu.add_command(label="Cadastrar", \
                    command=self.controle.insereCupom)
        self.cupomMenu.add_command(label="Consultar", \
                    command=self.controle.consultaCupom)        
        self.menubar.add_cascade(label="Cupom", \
                    menu=self.cupomMenu)  

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

        self.ctrlProduto = pr.CtrlProduto(self)
        self.ctrlCupom = cu.CtrlCupom(self)

        self.limite = LimitePrincipal(self.root, self) 

        self.root.title("Trab 15")
        # Inicia o mainloop
        self.root.mainloop()
       
    def insereProduto(self):
        self.ctrlProduto.insereProduto()

    def consultaProduto(self):
        self.ctrlProduto.consultaProduto()
        
    def insereCupom(self):
        self.ctrlCupom.insereCupom()
    
    def consultaCupom(self):
        self.ctrlCupom.consultaCupom()

    def salvaDados(self):
        self.ctrlProduto.salvaDados()
        self.ctrlCupom.salvaDados()
        self.root.destroy()

if __name__ == '__main__':
    c = ControlePrincipal()