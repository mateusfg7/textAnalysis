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
        if option == "--tag":
            if netCheck():
                getTags(client, readFile(file))
            else:
                netWarning()

        elif option == "--feeling":
            if netCheck():
                feelingAnalisys(client, readFile(file))
            else:
                netWarning()

        elif option == "--summarize":
            if netCheck():
                summarizeText(client, readFile(file))
            else:
                netWarning()

        elif option == "--count":
            if netCheck():
                countWords(client, readFile(file))
            else:
                netWarning()

        elif option == "--entity":
            if netCheck():
                entityRecognition(
                    client, readFile(file))
            else:
                netWarning()

        elif option == "--frequency":
            if netCheck():
                frequencyOfWords(client, readFile(file))
            else:
                netWarning()

    except IndexError:
        print(texts.menu())
