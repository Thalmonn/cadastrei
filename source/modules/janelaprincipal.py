from modules import janelaconfig
from modules import menu
import tkinter as tk

# Classe destinada a janela principal da aplicação.


class JanelaPrincipal(tk.Tk):

    # Constroi o objeto janela principal.

    def __init__(self):
        super().__init__()

        # Define propriedades da janela principal.
        JanelaPrincipal.title(self, 'Cadastrei')
        JanelaPrincipal.iconbitmap(self, './resources/img/icons/mainicon.ico')
        JanelaPrincipal.configure(self, bg='#185c37')

        # Configura dimensões da janela principal.
        configura_janela = janelaconfig.Janela(master=JanelaPrincipal)
        configura_janela.centraliza_tamanho(janela=self)
        JanelaPrincipal.grid_rowconfigure(self, 0, weight=1)
        JanelaPrincipal.grid_columnconfigure(self, 0, weight=1)

        # Implementa a logo principal na janela.
        self.logo_principal = tk.PhotoImage(file='./resources/img/logos/logomain.png')
        self.label_logo = tk.Label(self, image=self.logo_principal, bg='#185c37')
        self.label_logo.grid(row=0, column=0, sticky='n')

        # Implementa frames na janela principal.
        frame_principal = menu.MenuPrincipal(master=JanelaPrincipal)
        frame_principal.grid(sticky='', padx=120, pady=120)
