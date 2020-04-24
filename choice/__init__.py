import sys

from interface import texts

from utils.fileTreatment import readFile
from utils.connection import checkInternetConnection as netCheck
from utils.connection import internetFailWarning as netWarning

from functions.getTags import getTags
from functions.feelingAnalisys import feelingAnalisys
from functions.summarizeText import summarizeText
from functions.countWords import countWords
from functions.entityRecognition import entityRecognition
from functions.frequencyOfWords import frequencyOfWords
from functions.emailExtract import emailExtract


def choices(option, client, file):
    fileState = readFile(file)

    if fileState:
        try:
            if netCheck():
                if option == "--tag":
                    getTags(client, fileState)
                elif option == "--feeling":
                    feelingAnalisys(client, fileState)
                elif option == "--summarize":
                    summarizeText(client, fileState)
                elif option == "--count":
                    countWords(client, fileState)
                elif option == "--entity":
                    entityRecognition(
                        client, fileState)
                elif option == "--frequency":
                    frequencyOfWords(client, fileState)
                elif option == "--email":
                    emailExtract(client, fileState)
            else:
                netWarning()

        except IndexError:
            print(texts.menu())
    else:
        print(f'Arquivo "{file}" não encontrado!\n')
        print(texts.menu())
        sys.exit(1)
