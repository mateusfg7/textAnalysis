# GLOBAL MODULES
import sys

from os import system as terminal
from json import loads as str2json


# LOCAL MODULES
from interface import texts

from auth import getKey
from auth import createKey

from choice import choices

from utils.fileTreatment import readFile
from utils.fileTreatment import writeFile
from utils.colors import colors


print(f'Verificando dependencias...\n{colors["reset"]}')

try:
    import Algorithmia
    print(
        f'Algorithmia {colors["green"]}OK{colors["reset"]}'
    )
except ModuleNotFoundError:
    print(
        f'Algorithmia {colors["red"]}NOT FOUND{colors["reset"]}'
    )
    print(
        f'install: https://algorithmia.com/developers/clients/python{colors["reset"]}'
    )
    sys.exit(1)

try:
    import googletrans
    print(
        f'GoogleTrans {colors["green"]}OK{colors["reset"]}'
    )
except ModuleNotFoundError:
    print(
        f'GoogleTrans {colors["red"]}NOT FOUND{colors["reset"]}'
    )
    print(
        f'install: https://pypi.org/project/googletrans/{colors["reset"]}'
    )
    sys.exit(1)

keys = getKey(readFile, str2json)
if keys:
    CLIENT = Algorithmia.client(keys['api_key'])
else:
    print('Visite https://github.com/mateusfg7/textAnalysis/blob/master/README.md para saber como criar sua api key.')
    key = input('Sua api key: ')
    if createKey(key, writeFile):
        print('Api key salva com sucesso!')
        sys.exit()
    else:
        print('Um erro ocorreu durante o processo, tente novamente.')
        sys.exit()


terminal('clear')
print('Passe o caminho do arquivo de texto:')
file = input('> ')

terminal('clear')
print('Escolha uma função:')
print(
    '''
[1] Obter tags a partir de um texto.

[2] Obter grau de sentimentos positivos, negativos e neutros.

[3] Resumir um texto.

[4] Obter nomes de entidades presentes no texto.

[5] Obter a frequência de determinadas palavras em um texto.

[6] Contar número de palavras em um texto.

''')
choice = input('> ')

terminal('clear')
selectChoice = {
    '1': lambda: choices('tag', CLIENT, file),
    '2': lambda: choices('feeling', CLIENT, file),
    '3': lambda: choices('summarize', CLIENT, file),
    '4': lambda: choices('entity', CLIENT, file),
    '5': lambda: choices('frequency', CLIENT, file),
    '6': lambda: choices('count', CLIENT, file),
}
selectChoice[choice]()
