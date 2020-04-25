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


try:
    import Algorithmia
    keys = getKey(readFile, str2json)
    if keys:
        CLIENT = Algorithmia.client(keys['api_key'])
    else:
        print('Visite https://github.com/mateusfg7/textAnalysis/blob/master/README.md para saber como criar sua api key.')
        key = input('Sua api key: ')
        if createKey(key, writeFile):
            print('Api key salva com sucesso!')
            sys.exit()
        else:
            print('Um erro ocorreu durante o processo, tente novamente.')
            sys.exit()
except ModuleNotFoundError:
    print(texts.moduleNotFoundError('Algorithmia', 'algorithmia'))
    sys.exit(1)


arguments = sys.argv
rangeOfOptions = ['--tag', '--feeling', '--count', '--email',
                  '--frequency', '--entity', '--summarize', '--help', '-h']

if len(arguments) > 2:
    found = 0
    for option in rangeOfOptions:
        try:
            ARGUMENT_POSITION = arguments.index(option)
            FILE_ARGUMENT_POSITION = arguments.index('--file')
            choices(option, CLIENT,
                    arguments[FILE_ARGUMENT_POSITION + 1])
            found += 1
        except ValueError:
            pass
    if found == 0:
        print(texts.menu())
        sys.exit()

else:
    print(texts.menu())
    sys.exit()
