# Importação das bibliotecas e arquivos da aplicação.

from pathlib import Path
import tkinter as tk
from modules import janelaconfig

# Importa recursos para aplicação.

resources_folder = Path('cadastrei/resources')

# Cria e configura janela principal.

janela_principal = tk.Tk()  # Cria objeto janela principal.
janela_principal.title('Cadastrei')  # Define o título da janela.
config_janelaprincipal = janelaconfig.Janela(master=janela_principal)  # Acessa configuração janelaconfig.
config_janelaprincipal.centraliza_tamanho(janela=janela_principal)  # Centraliza a janela na tela.

# Inicia aplicação.

if __name__ == '__main__':
    janela_principal.mainloop()
