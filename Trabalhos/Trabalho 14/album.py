from cProfile import label
import tkinter as tk
from tkinter import messagebox, simpledialog
from tkinter import ttk
import pickle
import os.path

class Musica:
    def __init__(self, titulo, artista, album, nroFaixa):
        self.__titulo = titulo
        self.__artista = artista
        self.__album = album
        self.__nroFaixa = nroFaixa
        artista.addMusica(self)

    def getTitulo(self):
        return self.__titulo

    def getArtista(self):
        return self.__artista

    def getAlbum(self):
        return self.__album

    def getNroFaixa(self):
        return self.__nroFaixa
    
    def getFaixa(self):
        msg = "Musica: " + self.__titulo + "\n"
        msg += "N° Faixa: " + str(self.__nroFaixa) + "\n"
        msg += "---------" + "\n"
        return msg

class Album:
    def __init__(self, titulo, artista, ano):
        self.__titulo = titulo
        self.__artista = artista
        self.__ano = ano
        self.__faixas = []
        artista.addAlbum(self)

    def getTitulo(self):
        return self.__titulo

    def getArtista(self):
        return self.__artista

    def getAno(self):
        return self.__ano

    def getFaixas(self):
        return self.__faixas
    
    def addFaixa(self, titulo, artista=None):
        if artista == None:
            artista = self.__artista
        nroFaixa = len(self.__faixas) + 1
        musica = Musica(titulo, artista, self, nroFaixa)
        self.__faixas.append(musica)
        
    def getAlbum(self):
        msg = "Título: " + self.__titulo + "\n"
        msg += "Ano: " + str(self.__ano) + "\n"
        msg += "Faixas:" + str(len(self.getFaixas())) +"\n"
        for faixa in self.__faixas:
            msg += faixa.getFaixa()
        return msg
        
class LimiteInsereAlbum(tk.Toplevel):
    def __init__(self, controle, listaArtistas):

        tk.Toplevel.__init__(self)
        self.geometry('250x300')
        self.title("Criação de Album")
        self.controle = controle

        self.frameTitulo = tk.Frame(self)
        self.frameAno = tk.Frame(self)
        self.frameArtista = tk.Frame(self)
        self.frameMusica = tk.Frame(self)
        self.frameButton = tk.Frame(self)
        self.frameTitulo.pack()
        self.frameAno.pack()
        self.frameArtista.pack()
        self.frameMusica.pack()
        self.frameButton.pack()

        self.labelTitulo = tk.Label(self.frameTitulo,text="Título: ")
        self.labelTitulo.pack(side="left")
        self.inputTitulo = tk.Entry(self.frameTitulo)
        self.inputTitulo.pack(side="left")
        
        self.labelAno = tk.Label(self.frameAno,text="Ano: ")
        self.labelAno.pack(side="left")
        self.inputAno = tk.Entry(self.frameAno)
        self.inputAno.pack(side="left")
        
        self.labelArtista = tk.Label(self.frameArtista,text="Artista: ")
        self.labelArtista.pack(side="left")
        self.inputArtista = tk.StringVar()
        self.inputArtista = ttk.Combobox(self.frameArtista, width = 15 , textvariable = self.inputArtista)
        self.inputArtista.pack()
        self.inputArtista['values'] = listaArtistas
        
        self.labelMusica = tk.Label(self.frameMusica,text="N° Músicas: 0")
        self.labelMusica.pack(side="left")
        self.buttonAddMusica = tk.Button(self.frameMusica, text="Adicionar Música")
        self.buttonAddMusica.pack(side="left")
        self.buttonAddMusica.bind("<Button>", controle.adicionaMusica)
        
        self.buttonSubmit = tk.Button(self.frameButton ,text="Criar")      
        self.buttonSubmit.pack(side="left")
        self.buttonSubmit.bind("<Button>", controle.criarAlbum)
        
        self.buttonCancel = tk.Button(self.frameButton ,text="Cancelar")
        self.buttonCancel.pack(side="left")
        self.buttonCancel.bind("<Button>", controle.cancelar)

        self.buttonClear = tk.Button(self.frameButton ,text="Clear")      
        self.buttonClear.pack(side="left")
        self.buttonClear.bind("<Button>", controle.clear)

    def mostraJanela(self, titulo, msg):
        messagebox.showinfo(titulo, msg)
        
class LimiteConsultaAlbum(tk.Toplevel):
    def __init__(self, controle):

        tk.Toplevel.__init__(self)
        self.geometry('250x500')
        self.title("Consulta de Album")
        self.controle = controle

        self.frameInfo = tk.Frame(self)
        self.frameButton = tk.Frame(self)
        self.frameInfo.pack()
        self.frameButton.pack()

        self.labelInfo = tk.Label(self.frameInfo,text="")
        self.labelInfo.pack()
      
        self.buttonClear = tk.Button(self.frameButton ,text="Clear")      
        self.buttonClear.pack(side="left")
        self.buttonClear.bind("<Button>", controle.fecharConsultaArtista)  

    def mostraJanela(self, titulo, msg):
        messagebox.showinfo(titulo, msg)
        
class CtrlAlbum():       
    def __init__(self, controlePrincipal):
        self.ctrlPrincipal = controlePrincipal
        self.listaNomesMusica = []
        if not os.path.isfile("albums.pickle"):
            self.listaAlbums =  []
        else:
            with open("albums.pickle", "rb") as f:
                self.listaAlbums = pickle.load(f)
                
    def salvaDados(self):
        if len(self.listaAlbums) != 0:
            with open("albums.pickle","wb") as f:
                pickle.dump(self.listaAlbums, f)

    def insereAlbum(self):
        self.listaNomesMusica = []
        listaArtistas = self.ctrlPrincipal.ctrlArtista.getListaArtistasNome()
        self.limiteInsereAlbum = LimiteInsereAlbum(self, listaArtistas)
        
    def adicionaMusica(self, event):
        musicaNome = simpledialog.askstring("Adicionar Música", "Nome da Música: ")
        if musicaNome != None:
            self.listaNomesMusica.append(musicaNome)
            self.limiteInsereAlbum.labelMusica['text'] = "N° Músicas: " + str(len(self.listaNomesMusica))
        else:
            self.limiteInsereAlbum.mostraJanela("Erro", "Nome inválido")
    
    def criarAlbum(self, event):
        titulo = self.limiteInsereAlbum.inputTitulo.get()
        ano = self.limiteInsereAlbum.inputAno.get()
        artista = self.limiteInsereAlbum.inputArtista.get()
        
        if len(titulo) == 0 or len(ano) == 0 or len(artista) == 0:
            self.limiteInsereAlbum.mostraJanela("Erro", "Preencha todos os campos")
        elif self.ctrlPrincipal.ctrlArtista.getArtista(artista) == None: 
            self.limiteInsereAlbum.mostraJanela("Erro", "Artista não encontrado")
        else:
            album = Album(titulo, self.ctrlPrincipal.ctrlArtista.getArtista(artista), int(ano))
            for nomeMusica in self.listaNomesMusica:
                album.addFaixa(nomeMusica)
            self.listaAlbums.append(album)
            self.ctrlPrincipal.ctrlArtista.getArtista(artista).addAlbum(album)
            self.limiteInsereAlbum.mostraJanela("Album criado", "Album criado com sucesso!")
            self.limiteInsereAlbum.destroy()
            
    def cancelar(self, event):
        self.limiteInsereAlbum.destroy()
        
    def clear(self, event):
        self.limiteInsereAlbum.inputTitulo.delete(0, tk.END)
        self.limiteInsereAlbum.inputAno.delete(0, tk.END)
        self.limiteInsereAlbum.inputArtista.delete(0, tk.END)
        self.listaNomesMusica = []
        self.limiteInsereAlbum.labelMusica['text'] = "N° Músicas: 0"
        
    def getMusicas(self):
        listaMusicas = []
        for album in self.listaAlbums:
            for faixa in album.getFaixas():
                listaMusicas.append(faixa.getTitulo())
        return listaMusicas
    
    def getMusica(self, nome):
        for album in self.listaAlbums:
            for faixa in album.getFaixas():
                if faixa.getTitulo() == nome:
                    return faixa
        return None
    
    def consultaAlbum(self):
        nome = simpledialog.askstring("Nome", "Digite o nome do album:")
        if nome == None:
            self.ctrlPrincipal.limite.mostraJanela("Erro", "Nome não digitado")
            return
        
        for album in self.listaAlbums:
            if album.getTitulo() == nome:
                self.limiteConsultaAlbum = LimiteConsultaAlbum(self)
                self.limiteConsultaAlbum.labelInfo['text'] = album.getAlbum()
                return
            
        self.ctrlPrincipal.limite.mostraJanela("Erro", "Album não encontrado")
        
    def fecharConsultaArtista(self, event):
        self.limiteConsultaAlbum.destroy()