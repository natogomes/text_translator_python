import PySimpleGUI as sg
from dados import *


def tela_ini():
    sg.theme('DarkBlack')

    entrada = [
        [sg.Text('Idioma de entrada:', font='arial 13', pad=(0, 0))],
        [sg.InputCombo(idiomas, font='arial 13', size=(20, 1),
                       pad=(0, (0, 15)), key='entrada')],
    ]
    saida = [
        [sg.Text('Idioma de saída:', font='arial 13', pad=(0, 0))],
        [sg.InputCombo(idiomas, font='arial 13', size=(20, 1),
                       pad=(0, (0, 15)), key='saida')],
    ]

    layout = [
        [sg.Image('logoTradutor.png', pad=((0, 650), (8, 0)))],
        [sg.Column(entrada, element_justification='center'),
         sg.Text(' ' * 10),
         sg.Column(saida, element_justification='center')],
        [sg.Text('Digite aqui seu texto:', font='arial 13')],
        [sg.Multiline(font='arial 13', size=(80, 8), key='texto')],
        [sg.Button('Traduzir', font='arial 13 bold', size=(10, 1), pad=(5, (8, 15))),
         sg.Button('Limpar', font='arial 13', size=(8, 1), pad=(5, (8, 15)))],
        [sg.Text('Tradução:', font='arila 13')],
        [sg.Output(font='arial 13', size=(80, 8), key='traducao')],
        [sg.CButton('Sair', font='arial 13 bold', size=(8, 1), pad=(0, 8), button_color='red')]
    ]
    telaPrin = sg.Window('Translate', layout=layout, size=(850, 630), element_justification='center', finalize=True)


