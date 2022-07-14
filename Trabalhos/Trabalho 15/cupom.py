import tkinter as tk
from tkinter import messagebox, simpledialog
from tkinter import ttk
import pickle
import os.path

class Cupom:
    def __init__(self, codigo, produtos):
        self.codigo = codigo
        self.produtos = produtos
        
    def getCodigo(self):
        return self.codigo
    
    def getProdutos(self):
        return self.produtos
    
    def getCupom(self):
        msg = ""
        msg += "Codigo: " + self.codigo + "\n"
        msg += "----Produtos----\n"
        prints = []
        for prod in self.produtos:
            msg += "\n"
            quant = 0
            if prod.getCodigo() in prints:
                continue
            for item in self.produtos:
                if item == prod:
                    quant += 1
            msg += prod.getProduto(False)
            msg += "Quantidade: " + str(quant) + "\n"
            msg += "Valor Total: " + str(int(prod.getValorUnitario()) * quant) + "\n"
            prints.append(prod.getCodigo())
            
        return msg
                
    
class LimiteInsereCupom(tk.Toplevel):
    def __init__(self, controle, listaCuponsCod):

        tk.Toplevel.__init__(self)
        self.geometry('250x120')
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
        
        self.label2 = tk.Label(self.frame2,text="Insira Produtos: ")
        self.label2.pack(side="left")
        self.input2 = tk.StringVar()
        self.input2 = ttk.Combobox(self.frame2, width = 15 , textvariable = self.input2)
        self.input2.pack()
        self.input2['values'] = listaCuponsCod
        self.input2.current(0)
        
        self.label3 = tk.Label(self.frame3,text="N° Produtos: 0")
        self.label3.pack(side="left")
        self.button4 = tk.Button(self.frame3,text="Inserir")
        self.button4.pack(side="left")
        self.button4.bind("<Button-1>", controle.insereProduto)
        
        self.button1 = tk.Button(self.frame4 ,text="Fechar Cupom")   
        self.button1.pack(side="left")
        self.button1.bind("<Button>", controle.criarCupom)
        
        self.button2 = tk.Button(self.frame4 ,text="Cancelar")
        self.button2.pack(side="left")
        self.button2.bind("<Button>", controle.cancelar)

    def mostraJanela(self, titulo, msg):
        messagebox.showinfo(titulo, msg)
        
class CtrlCupom():       
    def __init__(self, controlePrincipal):
        self.ctrlPrincipal = controlePrincipal
        self.listaProdutos = []
        if not os.path.isfile("cupom.pickle"):
            self.listaCupons =  []
        else:
            with open("cupom.pickle", "rb") as f:
                self.listaCupons = pickle.load(f)
                
    def salvaDados(self):
        if len(self.listaCupons) != 0:
            with open("cupom.pickle","wb") as f:
                pickle.dump(self.listaCupons, f)
    
    def insereCupom(self):
        self.listaProdutos = []
        cods = ["--"]
        cods.extend(self.ctrlPrincipal.ctrlProduto.getProdutosCod())
        self.limiteIns = LimiteInsereCupom(self, cods)
        
    def insereProduto(self, event):
        codigo = self.limiteIns.input2.get()
        produto = self.ctrlPrincipal.ctrlProduto.getProduto(codigo)
        print(codigo)
        if produto == None:
            self.ctrlPrincipal.limite.mostraJanela("Erro", "Produto nao encontrado")
            return
        self.listaProdutos.append(produto)
        self.limiteIns.input2.current(0)
        self.limiteIns.label3["text"] = "N° Produtos: " + str(len(self.listaProdutos))

    def criarCupom(self, event):
        codigo = self.limiteIns.input1.get()
        
        if len(codigo) == 0:
            self.ctrlPrincipal.limiteIns.mostraJanela("Erro", "Codigo nao pode ser vazio")
            return
        
        if len(self.listaProdutos) == 0:
            self.ctrlPrincipal.limiteIns.mostraJanela("Erro", "Nao ha produtos para criar o cupom")
            return
        
        cupom = Cupom(codigo, self.listaProdutos)
        self.listaCupons.append(cupom)
        self.ctrlPrincipal.limite.mostraJanela("Cupom Criado", "Cupom criado com sucesso")
        self.limiteIns.destroy()
        
    def cancelar(self, event):
        self.limiteIns.destroy()
        
    def clear(self, event):
        self.limiteIns.input1.delete(0, tk.END)
        self.limiteIns.input2.delete(0, tk.END)
        self.limiteIns.input3.delete(0, tk.END)
        
    def consultaCupom(self):
        codigo = simpledialog.askstring("Consulta Cupom", "Digite o codigo do cupom")
        if codigo == None:
            return
        
        if len(codigo) == 0:
            self.ctrlPrincipal.limiteIns.mostraJanela("Erro", "Codigo nao pode ser vazio")
            return
        
        for cupom in self.listaCupons:
            if cupom.getCodigo() == codigo:
                self.ctrlPrincipal.limite.mostraJanela("Cupom - " + cupom.getCodigo(), cupom.getCupom())
                return
            
        self.ctrlPrincipal.limite.mostraJanela("Erro", "Cupom nao encontrado")