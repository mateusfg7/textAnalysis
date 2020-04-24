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
            if option == "--tag":
                if netCheck():
                    getTags(client, fileState)
                else:
                    netWarning()

            elif option == "--feeling":
                if netCheck():
                    feelingAnalisys(client, fileState)
                else:
                    netWarning()

            elif option == "--summarize":
                if netCheck():
                    summarizeText(client, fileState)
                else:
                    netWarning()

            elif option == "--count":
                if netCheck():
                    countWords(client, fileState)
                else:
                    netWarning()

            elif option == "--entity":
                if netCheck():
                    entityRecognition(
                        client, fileState)
                else:
                    netWarning()

            elif option == "--frequency":
                if netCheck():
                    frequencyOfWords(client, fileState)
                else:
                    netWarning()

            elif option == "--email":
                if netCheck():
                    emailExtract(client, fileState)
                else:
                    netWarning()

        except IndexError:
            print(texts.menu())
    else:
        print(f'Arquivo "{file}" não encontrado!\n')
        print(texts.menu())
        sys.exit(1)
