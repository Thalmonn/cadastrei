import tkinter as tk
from modules import janelaconfig

# Classe destinada ao formulário de cadastro.


class Formulario(tk.Toplevel):

    # Constroi o formulário

    def __init__(self):
        super().__init__()

        # Define propriedades do toplevel.
        Formulario.title(self, 'Ficha de Cadastro')
        Formulario.iconbitmap(self, './resources/img/icons/mainicon.ico')
        Formulario.configure(self, bg='#185c37')

        # Configura toplevel do formulário.
        conf_toplevel = janelaconfig.Janela(master=Formulario)
        conf_toplevel.centraliza_tamanho(janela=self)
        Formulario.grid_rowconfigure(self, 0, weight=1)
        Formulario.grid_columnconfigure(self, 0, weight=1)
