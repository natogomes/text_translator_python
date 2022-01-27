from translate import Translator

# pip install translate


def traducao(entrada, saida, texto):
    translator = Translator(from_lang=entrada, to_lang=saida)
    result = translator.translate(texto)
    print(result)
