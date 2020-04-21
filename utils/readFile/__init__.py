import sys


def readFile(file):
    try:
        with open(file, 'r') as openFile:
            return openFile.read()

    except FileNotFoundError:

        if file == 'analysis.py0':
            print('Nenhum arquivo foi passado!')
        else:
            print('Arquivo "{}" não encontrado!'.format(file))
        sys.exit()
