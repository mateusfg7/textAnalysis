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


cores = {
    'reset': '\033[0;0;0m',
    'red': '\033[1;31m',
    'liteRed': '\033[1;91m',
    'green': '\033[1;92m',
    'liteGreen': '\033[1;92m',
    'black': '\033[1;30m',
    'yellow': '\033[1;33m',
    'liteYellow': '\033[1;93m',
    'blue': '\033[1;34m',
    'liteBlue': '\033[1;94m',
    'magenta': '\033[1;35m',
    'magentaClaro': '\033[1;95m',
    'cyan': '\033[1;36m',
    'cyanClaro': '\033[1; 96m',
    'liteGray': '\033[1;37m',
    'darkGray': '\033[1;90m',
    'white': '\033[1;97m',
    'bold': '\033[;1m',
    'invert': '\033[;7m',
}

print(f'Verificando dependencias...\n{cores["reset"]}')

try:
    import Algorithmia
    print(
        f'Algorithmia {cores["green"]}OK{cores["reset"]}'
    )
except ModuleNotFoundError:
    print(
        f'Algorithmia {cores["red"]}NOT FOUND{cores["reset"]}'
    )
    print(
        f'install: https://algorithmia.com/developers/clients/python{cores["reset"]}'
    )
    sys.exit(1)

try:
    import googletrans
    print(
        f'GoogleTrans {cores["green"]}OK{cores["reset"]}'
    )
except ModuleNotFoundError:
    print(
        f'GoogleTrans {cores["red"]}NOT FOUND{cores["reset"]}'
    )
    print(
        f'install: https://pypi.org/project/googletrans/{cores["reset"]}'
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
    '4': lambda: choices('count', CLIENT, file),
    '5': lambda: choices('entity', CLIENT, file),
    '6': lambda: choices('frequency', CLIENT, file),
}
selectChoice[choice]()
