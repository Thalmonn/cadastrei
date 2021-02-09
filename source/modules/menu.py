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
                                 bg='#47c9a8',
                                 font='Roboto 12 bold',
                                 width=10,
                                 height=2,
                                 bd=5,
                                 relief='raised'
                                 )

        sair_sistema = tk.Button(self,
                                 text='Sair',
                                 bg='#de2701',
                                 font='Roboto 12 bold',
                                 width=10,
                                 height=2,
                                 bd=5,
                                 relief='raised'
                                 )

    # Layout

        cadastro_cliente.grid(row=1, column=0, sticky='n')
        ver_clientes.grid(row=2, column=0, sticky='')
        sair_sistema.grid(row=3, column=0, sticky='')

        # cadastro_cliente.grid_rowconfigure(1, weight=1)
        # cadastro_cliente.grid_columnconfigure(0, weight=1)
        # ver_clientes.grid_rowconfigure(2, weight=1)
        # ver_clientes.grid_columnconfigure(0, weight=1)
        # sair_sistema.grid_rowconfigure(3, weight=1)
        # sair_sistema.grid_columnconfigure(0, weight=1)
