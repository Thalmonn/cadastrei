import tkinter as tk
from PIL import Image, ImageTk

# Classe destinada ao menu principal da aplicação.


class MenuPrincipal(tk.Frame):

    # Constroi o frame do menu

    def __init__(self, master):  # Master será chamado na main.py
        super().__init__()

    # GUI
        # Botões

        # Icone do Botão Cadastrar
        icon_cadastroabre = Image.open('./resources/img/icons/cadastrocliente.ico')  # Carrega icone do botão.
        icon_cadastroabre = icon_cadastroabre.resize((30, 30), Image.ANTIALIAS)  # Redimensiona o icone.
        cadastro_icon = ImageTk.PhotoImage(icon_cadastroabre)  # Define icone do botão.

        # Icone do Botão Visualizar

        icon_verabre = Image.open('./resources/img/icons/vercliente.ico')  # Carrega icone do botão.
        icon_verabre = icon_verabre.resize((30, 30), Image.ANTIALIAS)  # Redimensiona o icone.
        ver_icon = ImageTk.PhotoImage(icon_verabre)  # Define icone do botão.

        # Icone do Botão Sair (apenas ajuste)

        sair_icon = tk.PhotoImage(width=1, height=1)

        # Config Botões

        cadastro_cliente = tk.Button(self,
                                     text='Cadastrar',
                                     compound='left',
                                     image=cadastro_icon,
                                     padx=10,
                                     bg='#d5fdec',
                                     font='Roboto 12 bold',
                                     width=120,
                                     height=50,
                                     bd=5,
                                     relief='raised'
                                     )

        cadastro_cliente.image = cadastro_icon  # Chama icone junto ao botão.

        ver_clientes = tk.Button(self,
                                 text='Visualizar',
                                 compound='left',
                                 image=ver_icon,
                                 padx=10,
                                 bg='#d5fdec',
                                 font='Roboto 12 bold',
                                 width=120,
                                 height=50,
                                 bd=5,
                                 relief='raised'
                                 )

        ver_clientes.image = ver_icon

        sair_sistema = tk.Button(self,
                                 text='Sair',
                                 compound='center',
                                 image=sair_icon,
                                 padx=10,
                                 bg='#d5fdec',
                                 font='Roboto 12 bold',
                                 width=120,
                                 height=50,
                                 bd=5,
                                 relief='raised'
                                 )

        sair_sistema.image = sair_icon

    # Layout

        cadastro_cliente.grid(row=1, column=0, sticky='')
        ver_clientes.grid(row=2, column=0, sticky='')
        sair_sistema.grid(row=3, column=0, sticky='')
