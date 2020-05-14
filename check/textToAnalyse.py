from typing import Union, NoReturn


def getTextToAnalyse() -> Union[str, NoReturn]:
    from utils.fileTreatment import readFile
    from utils.colors import style
    from interface import texts

    texts.clearAndShowHeader(style)
    print(texts.textToAnalyse(style))
    optionToAnalise = input('> ')

    if optionToAnalise == '1':
        texts.clearAndShowHeader(style)
        fileDirectory = input('Caminho do arquivo:\n> ')
        text = readFile(fileDirectory)
        if not text:
            print('Arquivo não encontrado!')
            sys.exit()
    else:
        texts.clearAndShowHeader(style)
        print('Texto a ser analizado:')
        text = input('> ')
    return text
