import sys

from interface import texts

try:
    from googletrans import Translator
    translator = Translator()
except ModuleNotFoundError:
    print(texts.moduleNotFoundError('GoogleTrans', 'googletrans'))
    sys.exit(1)


def traduzir(language, text):
    return translator.translate(text, dest=language).text
