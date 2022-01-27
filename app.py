import PySimpleGUI as sg
from telas import *
from funcao import *

tela_ini()
while True:
    window, event, values = sg.read_all_windows()

    if event == sg.WIN_CLOSED:
        break

    if event == 'Traduzir':
        if values['entrada'] == '' or values['saida'] == '' or values['texto'] == '':
            sg.Popup('Os valores não foram preenchidos corretamente!', font='arial 13',  title='ERRO')
        else:
            traducao(values['entrada'], values['saida'], values['texto'])

    if event == 'Limpar':
        window['texto'].update('')
        window['traducao'].update('')
