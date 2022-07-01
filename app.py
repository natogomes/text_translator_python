import PySimpleGUI as sg
from interface_grafica import *
from funcao import *

# ABRE A JANELA DO PROGRAMA
window_ini()
while True:
    window, event, values = sg.read_all_windows()

    if event == sg.WIN_CLOSED:
        break

    if event == 'Traduzir':
        if values['entrada'] == '' or values['saida'] == '' or values['texto'] == '':
            sg.Popup('Os campos não foram preenchidos corretamente!', font='arial 13',  title='ERRO',
                     icon='img/logoico.ico')
        else:
            traducao(values['entrada'], values['saida'], values['texto'])

    if event == 'Limpar Texto':
        window['texto'].update('')

    if event == 'Limpar Tradução':
        window['traducao'].update('')

