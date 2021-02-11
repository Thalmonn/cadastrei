import tkinter as tk

# Classe destinada ao formulário de cadastro.


class Formulario(tk.Toplevel):

    # Constroi o formulário

    def __init__(self):
        super().__init__()

        # Define propriedades do toplevel.
        Formulario.title(self, 'Ficha de Cadastro')
        Formulario.iconbitmap(self, './resources/img/icons/mainicon.ico')
        Formulario.configure(self, bg='#185c37')
