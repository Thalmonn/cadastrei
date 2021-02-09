# Importação das bibliotecas e arquivos da aplicação.

import tkinter as tk
from modules import *

# GUI.

# Janela Principal

janela_principal = tk.Tk()  # Cria objeto janela principal.
janela_principal.title('Cadastrei')  # Define o título da janela principal.
janela_principal.iconbitmap('resources/img/icons/mainicon.ico')  # Define o ícone da janela principal.
config_janelaprincipal = janelaconfig.Janela(master=janela_principal)  # Acessa configuração janelaconfig.
config_janelaprincipal.centraliza_tamanho(janela=janela_principal)  # Centraliza a janela na tela.
janela_principal['bg'] = '#185c37'

# Logo Principal

logo_principal = tk.PhotoImage(file='resources/img/logos/logomain.png')  # Define arquivo de logo.
label_logoprincipal = tk.Label(master=janela_principal, image=logo_principal,
                               bg='#185c37').grid(row=0, column=0, sticky='n')  # Posiciona logo.
janela_principal.grid_rowconfigure(0, weight=1)
janela_principal.grid_columnconfigure(0, weight=1)

# FRAMES

# Frame do Menu Principal

frame_menu = menu.MenuPrincipal(master=janela_principal)  # Insere menu na janela principal.

# Configura Layout.

frame_menu.grid(sticky='', padx=120, pady=120)  # Carrega o frame do menu principal.

# Inicia aplicação.

if __name__ == '__main__':
    janela_principal.mainloop()
