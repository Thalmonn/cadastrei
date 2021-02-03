from tkinter import *

# Coleta a geometria da janela.


def get_geometry(frame):
    geometry = frame.winfo_geometry()
    match = re.match(r'^(\d+)x(\d+)\+(\d+)\+(\d+)$', geometry)
    return [int(val) for val in match.group(*range(1, 5))]

# Centraliza a janela.


def centraliza_janela(root):
    """Deve ser chamada após inicialização total da aplicação,
    para que a janela root (raiz) tenha o tamanho certo."""
    #  Evita qualquer flikering até que a janela esteja no tamanho correto.
    root.attributes('-alpha', 0)


# Coleta o tamanho da tela(monitor) atualmente utilizado.
    # Janela com configuração de fullscreen para evitar conflitos.
    root.withdraw()
    root.attributes('-fullscreen', True)
    root.update_idletasks()
    (screen_width, screen_height, *_) = get_geometry(root)
    root.attributes('-fullscreen', False)

# Em seguida, restaura a dimensões corretas da janela.
    root.deiconify()
    root.update_idletasks()
    (window_width, window_height, *_) = get_geometry(root)

# Após coletar posição, define centro e atualiza a janela.
    pos_x = round(screen_width / 2 - window_width / 2)
    pos_y = round(screen_height / 2 - window_height / 2)
    root.geometry(f'+{pos_x}+{pos_y}')
    root.update_idletasks()

    root.attributes('-alpha', 1)
