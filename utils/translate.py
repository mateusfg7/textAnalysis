import sys

from utils.colors import style
from interface import texts

try:
    from googletrans import Translator
    translator = Translator()
except ModuleNotFoundError:
    print(texts.modules(style, 'googletrans', 'error'))
    sys.exit(1)


def traduzir(language: str, text: str) -> str:
    return translator.translate(text, dest=language).text
