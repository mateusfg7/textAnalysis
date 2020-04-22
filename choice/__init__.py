from interface import texts

from utils.readFile import readFile
from utils.connection import checkInternetConnection as netCheck
from utils.connection import internetFailWarning as netWarning

from functions.getTags import getTags
from functions.feelingAnalisys import feelingAnalisys
from functions.summarizeText import summarizeText
from functions.countWords import countWords
from functions.entityRecognition import entityRecognition
from functions.frequencyOfWords import frequencyOfWords


def choices(option, client, file):
    try:
        if option == "-t":
            if netCheck():
                getTags(client, readFile(file))
            else:
                netWarning()

        elif option == "-s":
            if netCheck():
                feelingAnalisys(client, readFile(file))
            else:
                netWarning()

        elif option == "-r":
            if netCheck():
                summarizeText(client, readFile(file))
            else:
                netWarning()

        elif option == "-c":
            if netCheck():
                countWords(client, readFile(file))
            else:
                netWarning()

        elif option == "-e":
            if netCheck():
                entityRecognition(
                    client, readFile(file))
            else:
                netWarning()

        elif option == "-f":
            if netCheck():
                frequencyOfWords(client, readFile(file))
            else:
                netWarning()

        elif option == "-h":
            print(texts.menu())

    except IndexError:
        print(texts.menu())
