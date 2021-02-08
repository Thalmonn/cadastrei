# Importação das bibliotecas e arquivos da aplicação.

import tkinter as tk
from modules import *

# Configura GUI.

# Janela Principal

janela_principal = tk.Tk()  # Cria objeto janela principal.
janela_principal.title('Cadastrei')  # Define o título da janela principal.
janela_principal.iconbitmap('resources/img/icons/mainicon.ico')  # Define o ícone da janela principal.
config_janelaprincipal = janelaconfig.Janela(master=janela_principal)  # Acessa configuração janelaconfig.
config_janelaprincipal.centraliza_tamanho(janela=janela_principal)  # Centraliza a janela na tela.
janela_principal['bg']= '#185c37'
logoprincipal = tk.PhotoImage(file='resources/img/logos/logomain.png')  # Define imagem de logo da aplicação.
label_logo = tk.Label(master=janela_principal, image=logoprincipal).grid(row=0,
                                                                         column=0,
                                                                         padx=50,
                                                                         pady=50,
                                                                         sticky='N'
                                                                         )  # Configura posição da logo.

# Frame de Menu

frame_menu = menu.MenuPrincipal(master=janela_principal)  # Insere menu na janela principal.

# Configura Layout.

frame_menu.grid()  # Chama o frame do menu principal.

# Inicia aplicação.

if __name__ == '__main__':
    janela_principal.mainloop()
