import sys

try:
    import Algorithmia
    CLIENT = Algorithmia.client('simC43S79CE5FQyQ35I6X8UWv3z1')
except ModuleNotFoundError:
    print("Biblioteca 'Algorithmia' não foi encontrada.")
    print("tente: pip3 install algorithmia")
    sys.exit(1)

from connection import checkInternetConnection as netCheck
from connection import internetFailWarning as netWarning

from functions.pegar_tags import pegar_tags
from functions.analise_de_sentimento import analise_de_sentimento
from functions.resumir_texto import resumir_texto
from functions.contar_palavras import contar_palavras
from functions.reconhecimento_de_entidades import reconhecimento_de_entidades
from functions.frequencia_de_palavras import frequencia_de_palavras


def ler_arquivo():

    arquivo = sys.argv[2]

    try:

        with open(arquivo, 'r') as openFile:
            return openFile.read()

    except FileNotFoundError:

        if arquivo == 'analysis.py0':
            print('Nenhum arquivo foi passado!')
        else:
            print('Arquivo "{}" não encontrado!'.format(arquivo))
        sys.exit()


def menu():
    print(
        """
    Use: analysis.py [opção] [arquivo]

    -t  pegar tags apartir de um texto

    -s  obter sentimentos negativos, positivos e neutros apartir de um texto

    -r  resumir um texto

    -c  contar palavras contidas em um texto

    -e  reconhecer nomes de entidades

    -f calcular a frequência das n palavras mais comuns de um texto
        analysis.py -f [arquivo] [numero de palavras analisadas]
    """
    )


def condicionais():
    try:
        if sys.argv[1] == "-t":
            if netCheck():
                pegar_tags(CLIENT, ler_arquivo())
            else:
                netWarning()

        elif sys.argv[1] == "-s":
            if netCheck():
                analise_de_sentimento(CLIENT, ler_arquivo())
            else:
                netWarning()

        elif sys.argv[1] == "-r":
            if netCheck():
                resumir_texto(CLIENT, ler_arquivo())
            else:
                netWarning()

        elif sys.argv[1] == "-c":
            if netCheck():
                contar_palavras(CLIENT, ler_arquivo())
            else:
                netWarning()

        elif sys.argv[1] == "-e":
            if netCheck():
                reconhecimento_de_entidades(CLIENT, ler_arquivo())
            else:
                netWarning()

        elif sys.argv[1] == "-f":
            if netCheck():
                frequencia_de_palavras(CLIENT, ler_arquivo())
            else:
                netWarning()

        elif sys.argv[1] == "-h":
            menu()

    except IndexError:
        menu()


# main execution
condicionais()
