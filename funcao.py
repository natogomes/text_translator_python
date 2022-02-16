from translate import Translator
from dados import *
# pip install translate


def traducao(entrada, saida, texto):
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
    result = translator.translate(texto)
    print(result)
