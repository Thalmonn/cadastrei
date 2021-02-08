import tkinter as tk

# Classe destinada ao menu principal da aplicação.


class MenuPrincipal(tk.Frame):

    # Constroi o frame do menu

    def __init__(self, master):  # Master será chamado na main.py
        super().__init__()

    # GUI
        # Botões
        cadastro_cliente = tk.Button(self,
                                     text='Cadastrar',
                                     bg='#33c481',
                                     font='Roboto 12 bold',
                                     width=10,
                                     height=2,
                                     bd=5,
                                     relief='raised'
                                     )

        ver_clientes = tk.Button(self,
                                 text='Visualizar',
                                 bg='#33c481',
                                 font='Roboto 12 bold',
                                 width=10,
                                 height=2,
                                 bd=5,
                                 relief='raised'
                                 )
    # Layout

        cadastro_cliente.grid(row=0, column=0)
        ver_clientes.grid(row=1, column=0)
