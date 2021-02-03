# Importando bibliotecas

import tkinter as tk
from modules import janelaconfig

# Criando janela de menu principal.

root = tk.Tk()
menu_principal = root

# Configuração dimensoes e centraliza a janela principal.

menu_principal.geometry(f'800x600')
janelaconfig.centraliza_janela(menu_principal)

# Inicializa aplicação.

if __name__ == '__main__':
    menu_principal.mainloop()
