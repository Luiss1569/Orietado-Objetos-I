import tkinter as tk
from tkinter import messagebox, simpledialog
from tkinter import ttk
import pickle
import os.path

class Artista:
    def __init__(self, nome):
        self.__nome = nome
        self.__albuns = []
        self.__musicas = []

    def getNome(self):
        return self.__nome
    
    def getAlbuns(self):
        return self.__albuns
    
    def getMusicas(self):
        return self.__musicas
    
    def addAlbum(self, album):
        for album in self.__albuns:
            if album.getTitulo() == album.getTitulo():
                return
        self.__albuns.append(album)

    def addMusica(self, musica):
        self.__musicas.append(musica)
        
    def getArtista(self):
        msg = ""
        msg += "Nome: " + self.__nome + "\n"
        msg += "Albuns:" + str(len(self.getAlbuns())) + " \n"
        for album in self.__albuns:
            msg += album.getAlbum() + "\n"
        return msg

class LimiteConsultaArtista(tk.Toplevel):
    def __init__(self, controle, nome):

        tk.Toplevel.__init__(self)
        self.geometry('250x500')
        self.title(nome)
        self.controle = controle

        self.frameInfo = tk.Frame(self)
        self.frameButton = tk.Frame(self)
        self.frameInfo.pack()
        self.frameButton.pack()

        self.labelInfo = tk.Label(self.frameInfo,text="")
        self.labelInfo.pack()
      
        self.buttonClear = tk.Button(self.frameButton ,text="Sair")      
        self.buttonClear.pack(side="left")
        self.buttonClear.bind("<Button>", controle.fecharConsultaArtista)  

    def mostraJanela(self, titulo, msg):
        messagebox.showinfo(titulo, msg)
        
class CtrlArtista():       
    def __init__(self, controlePrincipal):
        self.ctrlPrincipal = controlePrincipal
        if not os.path.isfile("artista.pickle"):
            self.listaArtistas =  []
        else:
            with open("artista.pickle", "rb") as f:
                self.listaArtistas = pickle.load(f)
                
    def salvaDados(self):
        if len(self.listaArtistas) != 0:
            with open("artista.pickle","wb") as f:
                pickle.dump(self.listaArtistas, f)

    def insereArtista(self):
        nome = simpledialog.askstring("Nome", "Digite o nome do artista:")
        for nomeCriados in self.getListaArtistasNome():
            if nome == nomeCriados:
                self.ctrlPrincipal.limite.mostraJanela("Artista", "Artista já cadastrado!")
                return
        if nome != None:
            artista = Artista(nome)
            self.listaArtistas.append(artista)
            self.ctrlPrincipal.limite.mostraJanela("Artista", "Artista criado com sucesso!")
        else:
            self.ctrlPrincipal.limite.mostraJanela("Artista", "Nome inválido!")
            
    def consultaArtista(self):
        nome = simpledialog.askstring("Nome", "Digite o nome do artista:")
        if nome != None:
            for artista in self.listaArtistas:
                if artista.getNome() == nome:
                    self.limiteConsulta = LimiteConsultaArtista(self, nome)
                    self.limiteConsulta.labelInfo.configure(text=artista.getArtista())
                    return
            self.ctrlPrincipal.limite.mostraJanela("Artista", "Artista não encontrado!")
        else:
            self.ctrlPrincipal.limite.mostraJanela("Artista", "Nome inválido!")
            
    def fecharConsultaArtista(self, event):
        self.limiteConsulta.destroy()
        self.limiteConsulta = None
        
    def getListaArtistasNome(self):
        listaNomes = []
        for artista in self.listaArtistas:
            listaNomes.append(artista.getNome())
        return listaNomes
    
    def getArtista(self, nome):
        for artista in self.listaArtistas:
            if artista.getNome() == nome:
                return artista
        return None