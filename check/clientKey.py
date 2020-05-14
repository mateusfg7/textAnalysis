from typing import Union, NoReturn


def getClientKey(Algorithmia: 'Module') -> Union['AlgorithmiaClient', NoReturn]:
    from json import loads as str2json
    from auth import getKey
    from utils.fileTreatment import readFile

    keys = getKey(readFile, str2json)
    if keys:
        return Algorithmia.client(keys['api_key'])
    else:
        texts.clearAndShowHeader(style)
        print('Visite https://github.com/mateusfg7/textAnalysis/blob/master/README.md para saber como criar sua api key.')
        key = input('Sua api key: ')
        if createKey(key, writeFile):
            print('Api key salva com sucesso!')
            keys = getKey(readFile, str2json)
            return Algorithmia.client(keys['api_key'])
        else:
            print('Um erro ocorreu durante o processo, tente novamente.')
            sys.exit()
