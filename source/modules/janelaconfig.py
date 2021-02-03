def centraliza_janela(menu_principal):
    menu_principal.update_idletasks()

    # Encontra resolução da tela.

    tela_largura = menu_principal.winfo_screenwidth()
    tela_altura = menu_principal.winfo_screenheight()

    # Define posição da janela.

    tamanho = tuple(int(_) for _ in menu_principal.geometry().split('+')[0].split('x'))
    x = tela_largura / 2 - tamanho[0] / 2
    y = tela_altura / 2 - tamanho[1] / 2

    menu_principal.geometry("+%d+%d" % (x, y))
