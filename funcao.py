import PySimpleGUI as sg
from translate import Translator
from dados import *

# pip install translate


def traducao(entrada, saida, texto):
    """
    -> Recebe os parâmetros e faz a tradução.
    :param entrada: Passa o idioma que vai ser digitado o texto para tradução.
    :param saida: Passa o idioma que vai ser traduzido o texto.
    :param texto: Passa o texto que vai ser traduzido.
    :return: Sem retorno.
    """
    cont = 0
    ent = 0
    sai = 0
    for i in idiomas:
        if entrada == i:
            ent = cont
        if saida == i:
            sai = cont
        cont += 1

    entrada = languages[ent]
    saida = languages[sai]
    translator = Translator(from_lang=entrada, to_lang=saida)
    try:
        result = translator.translate(texto)
    except OSError:
        sg.Popup('Verifique sua conexão com a internet.',
                 font='arial 12', title='ERRO', icon='img/logoico.ico')
    else:
        print(result)
