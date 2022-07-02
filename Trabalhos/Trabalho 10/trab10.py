import tkinter as tk
from tkinter import messagebox, simpledialog
import tkinter

class ModelCliente():
    def __init__(self, nome, email, codigo):
        self.__nome = nome
        self.__email = email
        self.__codigo = codigo

    def getNome(self):
        return self.__nome

    def getEmail(self):
        return self.__email
    
    def getCodigo(self):
        return self.__codigo
    
    def describer(self):
        return self.__codigo + ", " + self.__nome + ", " + self.__email
    
class View():
    def __init__(self, master, controller):
        self.controller = controller
        self.janela = tk.Frame(master)
        self.janela.pack()
        self.frame1 = tk.Frame(self.janela)
        self.frame2 = tk.Frame(self.janela)
        self.frame3 = tk.Frame(self.janela)
        self.frame4 = tk.Frame(self.janela)
        self.frame5 = tk.Frame(self.janela)
        self.frame6 = tk.Frame(self.janela)
        self.frame1.pack()
        self.frame2.pack()
        self.frame3.pack()
        self.frame4.pack()
        self.frame5.pack()
        self.frame6.pack()
      
        self.labelInfo1 = tk.Label(self.frame1,text="Codigo: ")
        self.labelInfo2 = tk.Label(self.frame2,text="Nome: ")
        self.labelInfo3 = tk.Label(self.frame3,text="Email: ")
        self.labelInfo1.pack(side="left")
        self.labelInfo2.pack(side="left")
        self.labelInfo3.pack(side="left")

        self.inputText1 = tk.Entry(self.frame1, width=20)
        self.inputText1.pack(side="left")
        self.inputText2 = tk.Entry(self.frame2, width=20)
        self.inputText2.pack(side="left")
        self.inputText3 = tk.Entry(self.frame3, width=20)
        self.inputText3.pack(side="left")         
      
        self.buttonSubmit = tk.Button(self.frame4,text="Enter")      
        self.buttonSubmit.pack(side="left")
        self.buttonSubmit.bind("<Button>", controller.enterHandler)
      
        self.buttonClear = tk.Button(self.frame4,text="Clear")      
        self.buttonClear.pack(side="left")
        self.buttonClear.bind("<Button>", controller.clearHandler)  
        
        self.buttonSearch = tk.Button(self.frame6,text="Search")
        self.buttonSearch.pack_forget()
        self.buttonSearch.bind("<Button>", controller.searchHandler)
        
        self.buttonReset = tk.Button(self.frame6,text="Reset")
        self.buttonReset.pack_forget()
        self.buttonReset.bind("<Button>", controller.resetHandler)
        
        self.lb1 = tk.Listbox(self.frame5, width=20)

        # Ex2: Acrescentar o botão para listar os clientes cadastrados           

    def mostraJanela(self, titulo, mensagem):
        messagebox.showinfo(titulo, mensagem)
        
    def addItem(self, item):
        self.lb1.insert("end", item.describer())
        self.lb1.pack(side="left")
        
        self.buttonSearch.pack(side="left")
        self.buttonReset.pack(side="left")
        
    def clearList(self):
        self.lb1.delete(0, tkinter.END)
        
    def renderList(self, lista):
        self.clearList()
        for item in lista:
            self.addItem(item)
            
    def renderSearchDialog(self):
        return simpledialog.askstring("Codigo", "Digite o codigo:", parent=self.janela)
      
class Controller():       
    def __init__(self):
        self.root = tk.Tk()
        self.root.geometry('300x400')
        self.listaClientes = []

        # Cria a view passando referência da janela principal e
        # de si próprio (controlador)
        self.view = View(self.root, self) 

        self.root.title("Exemplo MVC")
        # Inicia o mainloop
        self.root.mainloop()

    def enterHandler(self, event):
        codigoCli = self.view.inputText1.get()
        nomeCli = self.view.inputText2.get()
        emailCli = self.view.inputText3.get()
        if nomeCli == "" or emailCli == "" or codigoCli == "":
            self.view.mostraJanela('Erro', 'Preencha todos os campos')
            return
        
        for cliente in self.listaClientes:
            if cliente.getCodigo() == codigoCli:
                self.view.mostraJanela('Erro', 'Cliente ja cadastrado')
                self.clearHandler(event)
                return
        
        cliente = ModelCliente(nomeCli, emailCli, codigoCli)
        self.listaClientes.append(cliente)
        self.view.addItem(cliente)
        self.view.mostraJanela('Sucesso', 'Cliente cadastrado com sucesso')
        self.clearHandler(event)

    def clearHandler(self, event):
        self.view.inputText1.delete(0, len(self.view.inputText1.get()))
        self.view.inputText2.delete(0, len(self.view.inputText2.get()))
        self.view.inputText3.delete(0, len(self.view.inputText3.get()))
    
    # Ex2: implementar função para listar os clientes cadastrados
    # def clientesHandler(self, event):
    
    def searchHandler(self, event):
        codigoCli = self.view.renderSearchDialog()
        for cliente in self.listaClientes:
            if cliente.getCodigo() == codigoCli:
                self.view.mostraJanela('Sucesso', 'Cliente encontrado')
                self.view.renderList([cliente])
                break
        else:
            self.view.mostraJanela('Erro', 'Cliente não encontrado')
    
    def resetHandler(self, event):
        self.view.renderList(self.listaClientes)

if __name__ == '__main__':
    c = Controller()