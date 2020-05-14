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
from check.clientKey import getClientKey


if checkModules(texts, style):
    import Algorithmia
    import googletrans

CLIENT = getClientKey(Algorithmia)

texts.clearAndShowHeader(style)
print('Oquê você deseja analizar?')
print(texts.textToAnalyse(style))
optionToAnalise = input('> ')

if optionToAnalise == '1':
    texts.clearAndShowHeader(style)
    fileDirectory = input('Caminho do arquivo:\n> ')
    text = readFile(fileDirectory)
    if not text:
        print('Arquivo não encontrado!')
        sys.exit()
else:
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
