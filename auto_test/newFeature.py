import sys

from typing import NoReturn
import Algorithmia

from check.clientKey import getClientKey
from utils.fileTreatment import readFile


def newFeature():
    CLIENT = getClientKey(Algorithmia)
    TEXT_LoremIpsum = readFile('auto_test/text/loremIpsum.txt')
    TEXT_EmailAndAddress = readFile('auto_test/text/emailAndAddress.txt')
    TEXT_Turing = readFile('auto_test/text/turing.txt')

    print('\n> PLAIN TEXT')

    print('\n> WITH LOREM IPSUM TEXT')

    print('\n> WITH EMAIL AND ADDRES TEXT')

    print('\n> WITH TURING')
