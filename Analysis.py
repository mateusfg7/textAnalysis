# GLOBAL MODULES
import sys
from json import loads as str2json

# LOCAL MODULES
from interface import texts
from auth import getKey
from auth import createKey
from choice import choices
from utils.fileTreatment import readFile
from utils.fileTreatment import writeFile
from utils.colors import style
from check.checkModules import checkModules


if checkModules(texts, style):
    import Algorithmia
    import googletrans

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


texts.clearAndShowHeader(style)
print('Texto a ser analizado:')
text = input('> ')

texts.clearAndShowHeader(style)
print(texts.choicesMenu(style))
choice = input('> ')

texts.clearAndShowHeader(style)
selectChoice = {
    '1': lambda: choices('tag', CLIENT, text),
    '2': lambda: choices('feeling', CLIENT, text),
    '3': lambda: choices('summarize', CLIENT, text),
    '4': lambda: choices('entity', CLIENT, text),
    '5': lambda: choices('frequency', CLIENT, text),
    '6': lambda: choices('count', CLIENT, text),
    '7': lambda: choices('email', CLIENT, text),
}
selectChoice[choice]()
