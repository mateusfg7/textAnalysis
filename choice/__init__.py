from typing import NoReturn

from requests import get as request
import sys

from interface import texts

from utils.fileTreatment import readFile
from utils.connection import checkInternetConnection as netCheck

from functions.getTags import getTags
from functions.feelingAnalisys import feelingAnalisys
from functions.summarizeText import summarizeText
from functions.countWords import countWords
from functions.entityRecognition import entityRecognition
from functions.frequencyOfWords import frequencyOfWords
from functions.emailExtract import emailExtract
from functions.dateExtrac import dateExtractor


def choices(option: str, client: 'Client', text: str) -> NoReturn:

    try:
        if netCheck(request):

            "c: client ; t: text"
            optionSelect = {
                "tag": lambda c, t: getTags(c, t),
                "feeling": lambda c, t: feelingAnalisys(c, t),
                "summarize": lambda c, t: summarizeText(c, t),
                "count": lambda c, t: countWords(c, t),
                "entity": lambda c, t: entityRecognition(c, t),
                "frequency": lambda c, t: frequencyOfWords(c, t),
                "email": lambda c, t:  emailExtract(c, t),
                "date": lambda c, t: dateExtractor(c, t)
            }
            optionSelect[option](client, text)

        else:
            print("Você não tem conexão com a internet.")
            print(
                "Esse script precisa de conexão com a internet para ser executado.")
            sys.exit()
    except IndexError:
        print(texts.menu())
