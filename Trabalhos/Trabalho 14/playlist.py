import tkinter as tk
from tkinter import messagebox, simpledialog
from tkinter import ttk
import pickle
import os.path

class Playlist:
    def __init__(self, nome):
        self.__nome = nome
        self.__musicas = []

    def getNome(self):
        return self.__nome

    def getMusicas(self):
        return self.__musicas

    def addMusica(self, musica):
        self.__musicas.append(musica)
        
    def getPlaylist(self):
        msg = "Playlist: " + self.__nome + "\n"
        msg += "Musicas: \n"
        for musica in self.__musicas:
            msg += musica.getFaixa() + "\n"
        return msg
        
class LimiteCriaPlayList(tk.Toplevel):
    def __init__(self, controle, listaMusicas):

        tk.Toplevel.__init__(self)
        self.geometry('250x400')
        self.title("Cria Playlist")
        self.controle = controle

        self.frameNome = tk.Frame(self)
        self.frameMusicas = tk.Frame(self)
        self.frameButton = tk.Frame(self)
        self.frameNome.pack()
        self.frameMusicas.pack()
        self.frameButton.pack()
        
        self.labelNome = tk.Label(self.frameNome,text="Nome: ")
        self.labelNome.pack(side="left")
        self.inputNome = tk.Entry(self.frameNome)
        self.inputNome.pack(side="left")
        
        self.labelMusicas = tk.Label(self.frameMusicas,text="Musicas: ")
        self.labelMusicas.pack()
        self.listbox = tk.Listbox(self.frameMusicas)
        self.listbox.pack()
        for nome in listaMusicas:
            self.listbox.insert(tk.END, nome)
            
        self.buttonAddMusica = tk.Button(self.frameMusicas ,text="Add Musica")
        self.buttonAddMusica.pack(side="left")
        self.buttonAddMusica.bind("<Button>", controle.addMusica)
            
        self.buttonSubmit = tk.Button(self.frameButton ,text="Cria")
        self.buttonSubmit.pack(side="left")
        self.buttonSubmit.bind("<Button>", controle.criaPlaylist)
        
        self.buttonCancel = tk.Button(self.frameButton ,text="Cancela")
        self.buttonCancel.pack(side="left")
        self.buttonCancel.bind("<Button>", controle.fechaCriaPlaylist)
      
        self.buttonClear = tk.Button(self.frameButton ,text="Clear")      
        self.buttonClear.pack(side="left")
        self.buttonClear.bind("<Button>", controle.limpar)  

    def mostraJanela(self, titulo, msg):
        messagebox.showinfo(titulo, msg)
        
class LimiteConsultaAlbum(tk.Toplevel):
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
      
        self.buttonClear = tk.Button(self.frameButton ,text="Clear")      
        self.buttonClear.pack(side="left")
        self.buttonClear.bind("<Button>", controle.fecharConsultaAlbum)  

    def mostraJanela(self, titulo, msg):
        messagebox.showinfo(titulo, msg)
        
class CtrlPlaylist():       
    def __init__(self, controlePrincipal):
        self.ctrlPrincipal = controlePrincipal
        if not os.path.isfile("playlist.pickle"):
            self.listaPlaylists =  []
        else:
            with open("playlist.pickle", "rb") as f:
                self.listaPlaylists = pickle.load(f)
                
    def salvaDados(self):
        if len(self.listaPlaylists) != 0:
            with open("playlist.pickle","wb") as f:
                pickle.dump(self.listaPlaylists, f)
                
    def inserePlaylist(self):
        self.musicas = []
        musicasNome = self.ctrlPrincipal.ctrlAlbum.getMusicas()
        self.limiteIns = LimiteCriaPlayList(self, musicasNome)
    
    def addMusica(self, event):
        musicaSel = self.limiteIns.listbox.get(tk.ACTIVE)
        musica = self.ctrlPrincipal.ctrlAlbum.getMusica(musicaSel)
        self.limiteIns.listbox.delete(tk.ACTIVE)
        self.musicas.append(musica)
        
    def fechaCriaPlaylist(self, event):
        self.limiteIns.destroy()
        
    def limpar(self, event):
        self.limiteIns.destroy()
        self.musicas = []
        
    def criaPlaylist(self, event):
        nome = self.limiteIns.inputNome.get()
        if nome == "":
            self.limiteIns.mostraJanela("Erro", "Nome da playlist nao pode ser vazio")
            return
        if nome in [pl.getNome() for pl in self.listaPlaylists]:
            self.limiteIns.mostraJanela("Erro", "Playlist ja existe")
            return
        if len(self.musicas) == 0:
            self.limiteIns.mostraJanela("Erro", "Playlist nao pode ser vazia")
            return
        
        playlist = Playlist(nome)
        for musica in self.musicas:
            playlist.addMusica(musica)
        self.listaPlaylists.append(playlist)
        self.limiteIns.destroy()
        
    def consultaPlaylist(self):
        nome = simpledialog.askstring("Consulta Playlist", "Digite o nome da playlist")
        if nome == None:
            return
        for playlist in self.listaPlaylists:
            if playlist.getNome() == nome:
                self.limiteCons = LimiteConsultaAlbum(self, nome)
                self.limiteCons.labelInfo.configure(text=playlist.getPlaylist())
                return
        self.ctrlPrincipal.limite.mostraJanela("Erro", "Playlist nao existe")
        
    def fecharConsultaAlbum(self, event):
        self.limiteCons.destroy()