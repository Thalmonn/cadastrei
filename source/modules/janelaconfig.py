# Classe de configuração padrão de janela.

class Janela:

    def __init__(self, master=None):
        self.master = master
        self.master.attributes('-topmost', True)

    @staticmethod
    def centraliza_tamanho(janela):

        # Tamanho da janela principal.

        janela_largura = 800
        janela_altura = 600

        # Coleta informações do tamanho da tela (monitor).

        tela_largura = janela.winfo_screenwidth()
        tela_altura = janela.winfo_screenheight()

        # Define as coordenadas da posição da janela.

        x = (tela_largura / 2) - (janela_largura / 2)
        y = (tela_altura / 2) - (janela_altura / 2)

        # Representa geometria da janela.

        janela.geometry(f'{janela_largura}x{janela_altura}+{int(x)}+{int(y)}')
