from typing import NoReturn
import Algorithmia

from check.clientKey import getClientKey
from utils.fileTreatment import readFile


def newFeature():
    CLIENT = getClientKey(Algorithmia)
    TEXT_LoremIpsum = readFile('test/text/loremIpsum.txt')
    TEXT_EmailAndAddress = readFile('test/text/emailAndAddress.txt')
    TEXT_Turing = readFile('test/text/turing.txt')

    print('\n> PLAIN TEXT')

    print('\n> WITH LOREM IPSUM TEXT')

    print('\n> WITH EMAIL AND ADDRES TEXT')

    print('\n> WITH TURING')
