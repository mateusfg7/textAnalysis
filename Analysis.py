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

from kernel import kernel_start

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

kernel_start(
    getClientKey,
    getTextToAnalyse,
    texts,
    choices,
    Algorithmia,
    style
)
