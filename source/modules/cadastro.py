import tkinter as tk
from PIL import Image, ImageTk
import pygame
import time as delay
from modules import janelaconfig


# Classe destinada ao formulário de cadastro.


class Formulario(tk.Toplevel):

    # Constroi o formulário

    def __init__(self):
        super().__init__()

        # Define propriedades do toplevel.
        Formulario.title(self, 'Ficha de Cadastro')
        Formulario.iconbitmap(self, './resources/img/icons/mainicon.ico')
        Formulario.configure(self, bg='#185c37')

        # Configura toplevel do formulário.
        conf_toplevel = janelaconfig.Janela(master=Formulario)
        conf_toplevel.centraliza_tamanho(janela=self)
        Formulario.grid_rowconfigure(self, 0, weight=1)
        Formulario.grid_columnconfigure(self, 0, weight=1)

        # Frame destinado ao fomulário
        frame_cadastro = tk.Frame(self, bg='#185c37')
        frame_cadastro.grid(sticky='', padx=120, pady=120)

        # Labels destinados a cada entry.
        label_nome = tk.Label(frame_cadastro,
                              text='Nome:',
                              font='Roboto 12 bold',
                              fg='#ffffff',
                              bg='#185c37',
                              justify='left',
                              anchor='w'
                              )

        label_nascimento = tk.Label(frame_cadastro,
                                    text='Data de Nascimento:',
                                    font='Roboto 12 bold',
                                    fg='#ffffff',
                                    bg='#185c37',
                                    justify='left',
                                    anchor='w'
                                    )

        label_atividade = tk.Label(frame_cadastro,
                                   text='Atividade:',
                                   font='Roboto 12 bold',
                                   fg='#ffffff',
                                   bg='#185c37',
                                   justify='left',
                                   anchor='w'
                                   )

        label_endereco = tk.Label(frame_cadastro,
                                  text='Endereço:',
                                  font='Roboto 12 bold',
                                  fg='#ffffff',
                                  bg='#185c37',
                                  justify='left',
                                  anchor='w'
                                  )

        label_telefone = tk.Label(frame_cadastro,
                                  text='Telefone:',
                                  font='Roboto 12 bold',
                                  fg='#ffffff',
                                  bg='#185c37',
                                  justify='left',
                                  anchor='w'
                                  )

        label_email = tk.Label(frame_cadastro,
                               text='E-mail:',
                               font='Roboto 12 bold',
                               fg='#ffffff',
                               bg='#185c37',
                               justify='left',
                               anchor='w'
                               )

        label_rg = tk.Label(frame_cadastro,
                            text='RG:',
                            font='Roboto 12 bold',
                            fg='#ffffff',
                            bg='#185c37',
                            justify='left',
                            anchor='w'
                            )

        label_cpf = tk.Label(frame_cadastro,
                             text='CPF:',
                             font='Roboto 12 bold',
                             fg='#ffffff',
                             bg='#185c37',
                             justify='left',
                             anchor='w'
                             )

        # Botões

        # Icone do Botão salvarform.
        icon_salvarformabre = Image.open('./resources/img/icons/salvaricon.ico')  # Carrega icone do botão.
        icon_salvarformabre = icon_salvarformabre.resize((30, 30), Image.ANTIALIAS)  # Redimensiona o icone.
        salvarform_icon = ImageTk.PhotoImage(icon_salvarformabre)  # Define icone do botão.

        icon_retornamenumabre = Image.open('./resources/img/icons/returnmenu.ico')  # Carrega icone do botão.
        icon_retornamenumabre = icon_retornamenumabre.resize((30, 30), Image.ANTIALIAS)  # Redimensiona o icone.
        retornamenu_icon = ImageTk.PhotoImage(icon_retornamenumabre)  # Define icone do botão.

        botao_salvarform = tk.Button(self,
                                     text='Salvar',
                                     compound='left',
                                     image=salvarform_icon,
                                     padx=10,
                                     bg='#d5fdec',
                                     font='Roboto 12 bold',
                                     width=120,
                                     height=50,
                                     bd=5,
                                     relief='raised',
                                     command=save_form
                                     )
        botao_salvarform.image = salvarform_icon  # Chama icone junto ao botão.

        botao_retornamenu = tk.Button(self,
                                      text='Retornar',
                                      compound='left',
                                      image=retornamenu_icon,
                                      padx=10,
                                      bg='#d5fdec',
                                      font='Roboto 12 bold',
                                      width=120,
                                      height=50,
                                      bd=5,
                                      relief='raised',
                                      command=lambda: [retorna_menu(), self.destroy()]
                                      )
        botao_retornamenu.image = retornamenu_icon  # Chama icone junto ao botão.

        # Entrys referente a cada imput do formulário
        nome_campo = tk.Entry(frame_cadastro, width=80)
        nascimento_campo = tk.Entry(frame_cadastro, width=10)
        atividade_campo = tk.Entry(frame_cadastro, width=30)
        endereco_campo = tk.Entry(frame_cadastro, width=80)
        telefone_campo = tk.Entry(frame_cadastro, width=12)
        email_campo = tk.Entry(frame_cadastro, width=40)
        rg_campo = tk.Entry(frame_cadastro, width=7)
        cpf_campo = tk.Entry(frame_cadastro, width=11)

        # Layout

        # Labels
        label_nome.grid(row=0, column=0, sticky='e')
        label_nascimento.grid(row=1, column=0, sticky='e')
        label_atividade.grid(row=2, column=0, sticky='e')
        label_endereco.grid(row=3, column=0, sticky='e')
        label_telefone.grid(row=4, column=0, sticky='e')
        label_email.grid(row=5, column=0, sticky='e')
        label_rg.grid(row=6, column=0, sticky='e')
        label_cpf.grid(row=7, column=0, sticky='e')

        # Entrys
        nome_campo.grid(row=0, column=1, sticky='w')
        nascimento_campo.grid(row=1, column=1, sticky='w')
        atividade_campo.grid(row=2, column=1, sticky='w')
        endereco_campo.grid(row=3, column=1, sticky='w')
        telefone_campo.grid(row=4, column=1, sticky='w')
        email_campo.grid(row=5, column=1, sticky='w')
        rg_campo.grid(row=6, column=1, sticky='w')
        cpf_campo.grid(row=7, column=1, sticky='w')

        # Botões
        botao_salvarform.grid(row=8, column=1, sticky='se')
        botao_retornamenu.grid(row=8, column=0, sticky='sw')

# Funções

# Som do click no botão.


def click_sound():
    pygame.init()
    pygame.mixer.music.load('./resources/sound/mouseclick.wav')
    pygame.mixer.music.play()
    pygame.event.wait(timeout=1)

# Som de salvar formulário.


def save_sound():
    pygame.init()
    pygame.mixer.music.load('./resources/sound/saved.wav')
    pygame.mixer.music.play()
    pygame.event.wait(timeout=1)

# Realiza ações ao clicar.


def on_click():
    click_sound()

# Salva o formulário na database.


def save_form():
    save_sound()
    # Restante será implementado.

# Retorna a janela inicial.


def retorna_menu():
    on_click()
    delay.sleep(0.1)
