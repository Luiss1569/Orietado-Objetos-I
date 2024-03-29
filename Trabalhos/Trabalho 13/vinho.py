import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
import pickle
import os.path

class Vinho:
    def __init__(self, codigo, nome, tipo, variedade, origem, preco):
        self.codigo = codigo
        self.nome = nome
        self.tipo = tipo
        self.variedade = variedade
        self.origem = origem
        self.preco = preco
    
    def getCodigo(self):
        return self.codigo

    def getNome(self):
        return self.nome

    def getTipo(self):
        return self.tipo

    def getVariedade(self):
        return self.variedade

    def getOrigem(self):
        return self.origem

    def getPreco(self):
        return self.preco

    def getVinho(self):
        return "Nome: " + str(self.getNome())\
        + "\nCodigo: " + str(self.getCodigo())\
        + "\nTipo: " + str(self.getTipo())\
        + "\nVariedade: " + str(self.getVariedade())\
        + "\nOrigem: " + str(self.getOrigem())\
        + "\nPreço: " + str(self.getPreco())


class tipoInv(Exception):
    pass

class variedadeInv(Exception):
    pass

class origemInv(Exception):
    pass

class campoVazio(Exception):
    pass
    

class LimiteInsereVinho(tk.Toplevel):
    def __init__(self, controle):

        tk.Toplevel.__init__(self)
        self.geometry('250x200')
        self.title("Vinho")
        self.controle = controle

        self.frameCodigo = tk.Frame(self)
        self.frameNome = tk.Frame(self)
        self.frameTipo = tk.Frame(self)
        self.frameVariedade = tk.Frame(self)
        self.frameOrigem = tk.Frame(self)
        self.framePreco = tk.Frame(self)
        self.frameButton = tk.Frame(self)
        
        self.frameCodigo.pack()
        self.frameNome.pack()
        self.frameTipo.pack()
        self.frameVariedade.pack()
        self.frameOrigem.pack()
        self.framePreco.pack()
        self.frameButton.pack()
      
        self.labelCodigo = tk.Label(self.frameCodigo, text="Codigo: ")
        self.labelNome = tk.Label(self.frameNome,text="Nome: ")
        self.labelTipo = tk.Label(self.frameTipo, text="Tipo: ")
        self.labelVariedade = tk.Label(self.frameVariedade, text="Variedade: ")
        self.labelOrigem = tk.Label(self.frameOrigem, text="Origem: ")
        self.labelPreco = tk.Label(self.framePreco, text="Preco: ")
        self.labelCodigo.pack(side="left")
        self.labelNome.pack(side="left")
        self.labelTipo.pack(side="left")
        self.labelVariedade.pack(side="left")
        self.labelOrigem.pack(side="left")
        self.labelPreco.pack(side="left")

        self.inputCodigo = tk.Entry(self.frameCodigo, width=10)
        self.inputNome = tk.Entry(self.frameNome, width=20)
        self.inputTipo = tk.Entry(self.frameTipo, width=15)
        self.inputVariedade = tk.Entry(self.frameVariedade, width=20)
        self.inputOrigem = tk.Entry(self.frameOrigem, width=15)
        self.inputPreco = tk.Entry(self.framePreco, width=10)
        self.inputCodigo.pack(side="left")
        self.inputNome.pack(side="left")
        self.inputTipo.pack(side="left")
        self.inputVariedade.pack(side="left")
        self.inputOrigem.pack(side="left")
        self.inputPreco.pack(side="left")
      
        self.buttonSubmit = tk.Button(self.frameButton ,text="Enter")      
        self.buttonSubmit.pack(side="left")
        self.buttonSubmit.bind("<Button>", controle.enterHandler)
      
        self.buttonClear = tk.Button(self.frameButton ,text="Clear")      
        self.buttonClear.pack(side="left")
        self.buttonClear.bind("<Button>", controle.clearHandler)  

        self.buttonFecha = tk.Button(self.frameButton ,text="Concluído")      
        self.buttonFecha.pack(side="left")
        self.buttonFecha.bind("<Button>", controle.fechaHandler)

    def mostraJanela(self, titulo, msg):
        messagebox.showinfo(titulo, msg)

class LimiteConsultaVinho(tk.Toplevel):
     def __init__(self, controle, listaTipos, listaVariedades):

        tk.Toplevel.__init__(self)
        self.geometry('550x500')
        self.title("Vinho")
        self.controle = controle   

        self.frameBotoes = tk.Frame(self)
        self.frameVinhos = tk.Frame(self)
        
        self.labelTipo = tk.Label(self.frameBotoes, text="Tipo: ")
        self.labelVariedade = tk.Label(self.frameBotoes, text="Variedade: ")
        self.labelVinhos = tk.Label(self.frameVinhos, text="")
        
        self.comboTipo = ttk.Combobox(self.frameBotoes, values=listaTipos)
        self.comboTipo.bind("<<ComboboxSelected>>", controle.exibeTipo)
        self.comboVariedade = ttk.Combobox(self.frameBotoes, values=listaVariedades)
        self.comboVariedade.bind("<<ComboboxSelected>>", controle.exibeVariedade)
        
        self.frameBotoes.pack()
        self.labelTipo.pack(side="left")
        self.comboTipo.pack(side="left")
        self.labelVariedade.pack(side="left")
        self.comboVariedade.pack(side="left")
        self.frameVinhos.pack()
        self.labelVinhos.pack()
        
        self.comboTipo.current(0)
        self.comboVariedade.current(0)

class CtrlVinho():
    def __init__(self, controlador):
        self.controlador = controlador
        self.listaTipos = ["Branco", "Tinto", "Rose", "Espumante"]
        self.listaVar = ["Cabernet Sauvignon", "Carmenere", "Merlot", "Malbec", "Sauvignon Blanc", "Pinot Grigio"]
        self.listaPaises = ["Brasil", "Argentina", "Chile", "Itália", "França", "Portugal", "África do Sul"]

        if not os.path.isfile("vinhos.pickle"):
            self.listaVinhos =  []
        else:
            with open("vinhos.pickle", "rb") as f:
                self.listaVinhos = pickle.load(f)
                
    def salvaDados(self):
        with open("vinhos.pickle", "wb") as f:
            pickle.dump(self.listaVinhos, f)
    
    def cadastraVinho(self):
        self.limiteIns = LimiteInsereVinho(self)

    def consultaVinho(self):
        listaTipoCombo = ["Selecione"]
        listaTipoCombo.extend(self.listaTipos)
        listaVarCombo = ["Selecione"]
        listaVarCombo.extend(self.listaVar)
        self.limiteCons = LimiteConsultaVinho(self, listaTipoCombo, listaVarCombo)
    
    def enterHandler(self, event):
        codigo = self.limiteIns.inputCodigo.get()
        nome = self.limiteIns.inputNome.get()
        tipo = self.limiteIns.inputTipo.get()
        variedade = self.limiteIns.inputVariedade.get()
        origem = self.limiteIns.inputOrigem.get()
        preco = self.limiteIns.inputPreco.get()

        try:
            if codigo == '' or nome == '' or tipo == '' or variedade == '' or origem == '' or preco == '':
                raise campoVazio()
            elif tipo not in self.listaTipos:
                raise tipoInv()
            elif variedade not in self.listaVar:
                raise variedadeInv()
            elif origem not in self.listaPaises:
                raise origemInv()
        except campoVazio:
            self.limiteIns.mostraJanela('Erro', 'Preencha todos os campos')
        except tipoInv:
            self.limiteIns.mostraJanela('Erro','Tipo de vinho inválido')  
        except variedadeInv:
            self.limiteIns.mostraJanela('Erro','Variedade de vinho inválida')
        except origemInv:
            self.limiteIns.mostraJanela('Erro','Origem de vinho inválida')
        else:
            vinho = Vinho(codigo, nome, tipo, variedade, origem, preco)
            self.listaVinhos.append(vinho)
            self.limiteIns.mostraJanela('Sucesso', 'Vinho cadastrado com sucesso')
            self.clearHandler(event)
    
    def clearHandler(self, event):
        self.limiteIns.inputCodigo.delete(0, len(self.limiteIns.inputCodigo.get()))
        self.limiteIns.inputNome.delete(0, len(self.limiteIns.inputNome.get()))
        self.limiteIns.inputTipo.delete(0, len(self.limiteIns.inputTipo.get()))
        self.limiteIns.inputVariedade.delete(0, len(self.limiteIns.inputVariedade.get()))
        self.limiteIns.inputOrigem.delete(0, len(self.limiteIns.inputOrigem.get()))
        self.limiteIns.inputPreco.delete(0, len(self.limiteIns.inputPreco.get()))
    
    def fechaHandler(self, event):
        self.limiteIns.destroy()

    def exibeTipo(self,event):
        tipo = self.limiteCons.comboTipo.get()
        self.limiteCons.comboVariedade.current(0)
        msg = ''
        for vinho in self.listaVinhos:
            if vinho.getTipo() == tipo:
                msg +='-------\n'
                msg += vinho.getVinho() + '\n'
                msg +='-------\n'

        self.limiteCons.labelVinhos.configure(text=msg)
        
    def exibeVariedade(self, event):
        variedade = self.limiteCons.comboVariedade.get()
        self.limiteCons.comboTipo.current(0)
        msg = ''
        for vinho in self.listaVinhos:
            if vinho.getVariedade() == variedade:
                msg +='-------\n'
                msg += vinho.getVinho() + '\n'
                msg +='-------\n'
        
        self.limiteCons.labelVinhos.configure(text=msg)
