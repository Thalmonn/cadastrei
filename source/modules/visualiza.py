import tkinter as tk
from PIL import Image, ImageTk
import pygame
import time as delay
from openpyxl import *
from modules import janelaconfig
import os

# Função inicial destinada a verificar existencia da database.

if os.path.exists('./database/database.xlsx'):
    database = load_workbook('./database/database.xlsx')
    formcadastro = database.active
else:
    database = Workbook()
    formcadastro = database.active

# Classe destinada a visualização da database.


class MostraData(tk.Toplevel):

    # Constroi o objeto MostraData.

    def __init__(self):
        super().__init__()

        # Define propriedades do toplevel.
        MostraData.title(self, 'Visualizando Database')
        MostraData.iconbitmap(self, './resources/img/icons/mainicon.ico')
        MostraData.configure(self, bg='#185c37')

        # Configura toplevel do formulário.
        conf_toplevel = janelaconfig.Janela(master=MostraData)
        conf_toplevel.centraliza_tamanho(janela=self)
        MostraData.grid_rowconfigure(self, 0, weight=1)
        MostraData.grid_columnconfigure(self, 0, weight=1)

        # Frame destinado as informações da database.
        frame_db = tk.Frame(self, bg='#185c37')
        frame_db.grid(sticky='', padx=2, pady=2)

        # Cria variáveis para cada coluna.
        coluna_a = formcadastro['A']
        coluna_b = formcadastro['B']
        coluna_c = formcadastro['C']
        coluna_d = formcadastro['D']
        coluna_e = formcadastro['E']
        coluna_f = formcadastro['F']
        coluna_g = formcadastro['G']
        coluna_h = formcadastro['H']

        # Define funções que atualiza a visualização dos dados na GUI.

        def atualiza_dados():
            lista = ''
            for cell in coluna_a:
                lista = f'{lista + str(cell.value)}\n'

            label_a.config(text=lista)

            lista2 = ''
            for cell in coluna_b:
                lista2 = f'{lista2 + str(cell.value)}\n'

            label_b.config(text=lista2)

            lista3 = ''
            for cell in coluna_c:
                lista3 = f'{lista3 + str(cell.value)}\n'

            label_c.config(text=lista3)

            lista4 = ''
            for cell in coluna_d:
                lista4 = f'{lista4 + str(cell.value)}\n'

            label_d.config(text=lista4)

            lista5 = ''
            for cell in coluna_e:
                lista5 = f'{lista5 + str(cell.value)}\n'

            label_e.config(text=lista5)

            lista6 = ''
            for cell in coluna_f:
                lista6 = f'{lista6 + str(cell.value)}\n'

            label_f.config(text=lista6)

            lista7 = ''
            for cell in coluna_g:
                lista7 = f'{lista7 + str(cell.value)}\n'

            label_g.config(text=lista7)

            lista8 = ''
            for cell in coluna_h:
                lista8 = f'{lista8 + str(cell.value)}\n'

            label_h.config(text=lista8)

        # Botões

        # Icone do Botão Mostrar Database
        icon_mostrarabre = Image.open('./resources/img/icons/imprimir.ico')  # Carrega icone do botão.
        icon_mostrarabre = icon_mostrarabre.resize((30, 30), Image.ANTIALIAS)  # Redimensiona o icone.
        mostrar_icon = ImageTk.PhotoImage(icon_mostrarabre)  # Define icone do botão.

        mostrar_db = tk.Button(self,
                               text='Exibir Database',
                               compound='left',
                               image=mostrar_icon,
                               padx=10,
                               bg='#d5fdec',
                               font='Roboto 12 bold',
                               width=145,
                               height=50,
                               bd=5,
                               relief='raised',
                               command=lambda: [on_click(), atualiza_dados()]
                               )

        mostrar_db.image = mostrar_icon

        mostrar_db.grid(row=0, column=0, sticky='se')

        # Icone do Botão Voltar
        icon_voltarabre = Image.open('./resources/img/icons/returnmenu.ico')  # Carrega icone do botão.
        icon_voltarabre = icon_voltarabre.resize((30, 30), Image.ANTIALIAS)  # Redimensiona o icone.
        voltar_icon = ImageTk.PhotoImage(icon_voltarabre)  # Define icone do botão.

        voltar_menu = tk.Button(self,
                                text='Voltar',
                                compound='left',
                                image=voltar_icon,
                                padx=10,
                                bg='#d5fdec',
                                font='Roboto 12 bold',
                                width=120,
                                height=50,
                                bd=5,
                                relief='raised',
                                command=lambda: [retorna_menu(), self.destroy()]
                                )

        voltar_menu.image = voltar_icon

        voltar_menu.grid(row=0, column=0, sticky='sw')

        # Labels com informações da database.
        label_a = tk.Label(frame_db, text='', font='Roboto 8 bold', bg='#185c37', fg='#ffffff',
                           relief='ridge')
        label_a.grid(row=1, column=1, sticky='s')

        label_b = tk.Label(frame_db, text='', font='Roboto 8 bold', bg='#185c37', fg='#ffffff',
                           relief='ridge')
        label_b.grid(row=1, column=2, sticky='s')

        label_c = tk.Label(frame_db, text='', font='Roboto 8 bold', bg='#185c37', fg='#ffffff',
                           relief='ridge')
        label_c.grid(row=1, column=3, sticky='s')

        label_d = tk.Label(frame_db, text='', font='Roboto 8 bold', bg='#185c37', fg='#ffffff',
                           relief='ridge')
        label_d.grid(row=1, column=4, sticky='s')

        label_e = tk.Label(frame_db, text='', font='Roboto 8 bold', bg='#185c37', fg='#ffffff',
                           relief='ridge')
        label_e.grid(row=1, column=5, sticky='s')

        label_f = tk.Label(frame_db, text='', font='Roboto 8 bold', bg='#185c37', fg='#ffffff',
                           relief='ridge')
        label_f.grid(row=1, column=6, sticky='s')

        label_g = tk.Label(frame_db, text='', font='Roboto 8 bold', bg='#185c37', fg='#ffffff',
                           relief='ridge')
        label_g.grid(row=1, column=7, sticky='s')

        label_h = tk.Label(frame_db, text='', font='Roboto 8 bold', bg='#185c37', fg='#ffffff',
                           relief='ridge')
        label_h.grid(row=1, column=8, sticky='s')

# Funções Gerais

# Som do click no botão.


def click_sound():
    pygame.init()
    pygame.mixer.music.load('./resources/sound/mouseclick.wav')
    pygame.mixer.music.play()
    pygame.event.wait(timeout=1)

# Realiza ações ao clicar.


def on_click():
    click_sound()

# Retorna a janela inicial.


def retorna_menu():
    on_click()
    delay.sleep(0.1)
