import tkinter as tk
from tkinter import messagebox, simpledialog
from tkinter import ttk
import pickle
import os.path

class Produto:
    def __init__(self, codigo, descricao, valorUnitario):
        self.codigo = codigo
        self.descricao = descricao
        self.valorUnitario = valorUnitario
        
    def getCodigo(self):
        return self.codigo
    
    def getDescricao(self):
        return self.descricao
    
    def getValorUnitario(self):
        return self.valorUnitario
    
    def getProduto(self, valorUnitario=True):
        msg = ""
        msg += "Codigo: " + self.codigo + "\n"
        msg += "Descricao: " + self.descricao + "\n"
        
        if valorUnitario:
            msg += "Valor Unitario: " + str(self.valorUnitario) + "\n"
        
        return msg
    
class LimiteInsereProduto(tk.Toplevel):
    def __init__(self, controle,):

        tk.Toplevel.__init__(self)
        self.geometry('250x300')
        self.title("Criação de Album")
        self.controle = controle

        self.frame1 = tk.Frame(self)
        self.frame2 = tk.Frame(self)
        self.frame3 = tk.Frame(self)
        self.frame4 = tk.Frame(self)
        self.frame1.pack()
        self.frame2.pack()
        self.frame3.pack()
        self.frame4.pack()

        self.label1 = tk.Label(self.frame1,text="Codigo: ")
        self.label1.pack(side="left")
        self.input1 = tk.Entry(self.frame1)
        self.input1.pack(side="left")
        
        self.label2 = tk.Label(self.frame2,text="Descricao: ")
        self.label2.pack(side="left")
        self.input2 = tk.Entry(self.frame2)
        self.input2.pack(side="left")
        
        self.label3 = tk.Label(self.frame3,text="Valor Unitario: ")
        self.label3.pack(side="left")
        self.input3 = tk.Entry(self.frame3)
        self.input3.pack(side="left")
        
        self.button1 = tk.Button(self.frame4 ,text="Criar")      
        self.button1.pack(side="left")
        self.button1.bind("<Button>", controle.criarProduto)
        
        self.button2 = tk.Button(self.frame4 ,text="Cancelar")
        self.button2.pack(side="left")
        self.button2.bind("<Button>", controle.cancelar)

        self.button3 = tk.Button(self.frame4 ,text="Clear")      
        self.button3.pack(side="left")
        self.button3.bind("<Button>", controle.clear)

    def mostraJanela(self, titulo, msg):
        messagebox.showinfo(titulo, msg)
        
class CtrlProduto():       
    def __init__(self, controlePrincipal):
        self.ctrlPrincipal = controlePrincipal
        if not os.path.isfile("produto.pickle"):
            self.listaProdutos =  []
        else:
            with open("produto.pickle", "rb") as f:
                self.listaProdutos = pickle.load(f)
                
    def salvaDados(self):
        if len(self.listaProdutos) != 0:
            with open("produto.pickle","wb") as f:
                pickle.dump(self.listaProdutos, f)
    
    def insereProduto(self):
        self.limiteIns = LimiteInsereProduto(self)

    def criarProduto(self, event):
        codigo = self.limiteIns.input1.get()
        descricao = self.limiteIns.input2.get()
        valor = self.limiteIns.input3.get()
        
        for prod in self.listaProdutos:
            if prod.getCodigo() == codigo:
                self.limiteIns.mostraJanela("Erro", "Codigo ja existente")
                return
        
        produto = Produto(codigo, descricao, valor)
        self.listaProdutos.append(produto)
        self.limiteIns.mostraJanela("Sucesso", "Produto criado com sucesso")
        self.clear(event)
        
    def cancelar(self, event):
        self.limiteIns.destroy()
        
    def clear(self, event):
        self.limiteIns.input1.delete(0, tk.END)
        self.limiteIns.input2.delete(0, tk.END)
        self.limiteIns.input3.delete(0, tk.END)
        
    def consultaProduto(self):
        codigo = simpledialog.askstring("Consulta", "Digite o codigo do produto")
        
        for prod in self.listaProdutos:
            if prod.getCodigo() == codigo:
                self.ctrlPrincipal.limite.mostraJanela("Produto", prod.getProduto())
                return
            
        self.ctrlPrincipal.limite.mostraJanela("Erro", "Produto nao encontrado")
        
    def getProdutosCod(self):
        listaCod = []
        for prod in self.listaProdutos:
            listaCod.append(prod.getCodigo())
        return listaCod
    
    def getProduto(self, codigo):
        for prod in self.listaProdutos:
            if prod.getCodigo() == codigo:
                return prod
        return None
    
    def getProdutos(self):
        return self.listaProdutos