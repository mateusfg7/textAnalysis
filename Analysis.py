# types
from typing import Callable, Union, NoReturn, Dict

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
from check.textToAnalyse import getTextToAnalyse


# <start> rules for test
try:
    from auto_test.newFeature import newFeature
    arguments = sys.argv
    testFlags = {
        '-tf': lambda: newFeature(),
    }
    testFlags[arguments[1]]()
    exit()
except IndexError:
    pass
# <end> rules for test

if checkModules(texts, style):
    import Algorithmia
    import googletrans


def start(getClientKey: Callable[['Module'], Union['AlgorithmiaClient', NoReturn]],
          getTextToAnalyse: Callable[[], Union[str, NoReturn]],
          texts: Callable[[Dict[str, str]], NoReturn],
          choices: Callable[[str, 'Client', str], NoReturn],
          Algorithmia: 'Module',
          style: Dict[str, str]) -> NoReturn:
    """
        The kernel of algorithm
        """
    CLIENT = getClientKey(Algorithmia)
    TEXT = getTextToAnalyse()

    texts.clearAndShowHeader(style)
    print(texts.choicesMenu(style))
    choice = input('> ')

    texts.clearAndShowHeader(style)
    selectChoice = {
        '1': lambda: choices('tag', CLIENT, TEXT),
        '2': lambda: choices('feeling', CLIENT, TEXT),
        '3': lambda: choices('summarize', CLIENT, TEXT),
        '4': lambda: choices('entity', CLIENT, TEXT),
        '5': lambda: choices('frequency', CLIENT, TEXT),
        '6': lambda: choices('count', CLIENT, TEXT),
        '7': lambda: choices('email', CLIENT, TEXT),
        '8': lambda: choices('date', CLIENT, TEXT)
    }
    selectChoice[choice]()


if __name__ == "__main__":
    start(
        getClientKey,
        getTextToAnalyse,
        texts,
        choices,
        Algorithmia,
        style
    )
