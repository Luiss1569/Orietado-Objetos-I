import tkinter as tk
from tkinter import messagebox
import artista as ar
import album as al
import playlist as pl

class LimitePrincipal():
    def __init__(self, root, controle):
        self.controle = controle
        self.root = root
        self.root.geometry('300x250')
        self.menubar = tk.Menu(self.root)        
        self.artistaMenu = tk.Menu(self.menubar)
        self.albumMenu = tk.Menu(self.menubar)
        self.playlistMenu = tk.Menu(self.menubar)
        self.sairMenu = tk.Menu(self.menubar)    

        self.artistaMenu.add_command(label="Cadastrar", \
                    command=self.controle.insereArtista)
        self.artistaMenu.add_command(label="Consultar", \
            command=self.controle.consultarArtista)
        self.menubar.add_cascade(label="Artista", \
                    menu=self.artistaMenu)

        self.albumMenu.add_command(label="Cadastrar", \
                    command=self.controle.insereAlbum)
        self.albumMenu.add_command(label="Consultar", \
                    command=self.controle.consultarAlbum)        
        self.menubar.add_cascade(label="Album", \
                    menu=self.albumMenu)

        self.playlistMenu.add_command(label="Cadastrar", \
                    command=self.controle.inserePlaylist)
        self.playlistMenu.add_command(label="Consultar", \
                    command=self.controle.consultarPlaylist)                
        self.menubar.add_cascade(label="Playlist", \
                    menu=self.playlistMenu)        

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

        self.ctrlArtista = ar.CtrlArtista(self)
        self.ctrlAlbum = al.CtrlAlbum(self)
        self.ctrlPlayList = pl.CtrlPlaylist(self)

        self.limite = LimitePrincipal(self.root, self) 

        self.root.title("Trab 14")
        # Inicia o mainloop
        self.root.mainloop()
       
    def insereArtista(self):
        self.ctrlArtista.insereArtista()

    def consultarArtista(self):
        self.ctrlArtista.consultaArtista()
        
    def insereAlbum(self):
        self.ctrlAlbum.insereAlbum()
    
    def consultarAlbum(self):
        self.ctrlAlbum.consultaAlbum()
        
    def inserePlaylist(self):
        self.ctrlPlayList.inserePlaylist()
        
    def consultarPlaylist(self):
        self.ctrlPlayList.consultaPlaylist()

    def salvaDados(self):
        self.ctrlArtista.salvaDados()
        self.ctrlPlayList.salvaDados()
        self.ctrlAlbum.salvaDados()
        self.root.destroy()

if __name__ == '__main__':
    c = ControlePrincipal()