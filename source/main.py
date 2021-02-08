# Importação das bibliotecas e arquivos da aplicação.

import tkinter as tk
from modules import *

# Configura GUI.

janela_principal = tk.Tk()  # Cria objeto janela principal.
janela_principal.title('Cadastrei')  # Define o título da janela.
janela_principal.iconbitmap('resources/img/icons/mainicon.ico')  # Define o ícone da janela principal.
config_janelaprincipal = janelaconfig.Janela(master=janela_principal)  # Acessa configuração janelaconfig.
config_janelaprincipal.centraliza_tamanho(janela=janela_principal)  # Centraliza a janela na tela.

# Inicia aplicação.

if __name__ == '__main__':
    janela_principal.mainloop()
