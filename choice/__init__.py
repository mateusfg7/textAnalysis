from utils.readFile import readFile
from utils.connection import checkInternetConnection as netCheck
from utils.connection import internetFailWarning as netWarning

from functions.pegar_tags import pegar_tags
from functions.analise_de_sentimento import analise_de_sentimento
from functions.resumir_texto import resumir_texto
from functions.contar_palavras import contar_palavras
from functions.reconhecimento_de_entidades import reconhecimento_de_entidades
from functions.frequencia_de_palavras import frequencia_de_palavras


def condicionais(option, client, file):
    try:
        if option == "-t":
            if netCheck():
                pegar_tags(client, readFile(file))
            else:
                netWarning()

        elif option == "-s":
            if netCheck():
                analise_de_sentimento(client, readFile(file))
            else:
                netWarning()

        elif option == "-r":
            if netCheck():
                resumir_texto(client, readFile(file))
            else:
                netWarning()

        elif option == "-c":
            if netCheck():
                contar_palavras(client, readFile(file))
            else:
                netWarning()

        elif option == "-e":
            if netCheck():
                reconhecimento_de_entidades(
                    client, readFile(file))
            else:
                netWarning()

        elif option == "-f":
            if netCheck():
                frequencia_de_palavras(client, readFile(file))
            else:
                netWarning()

        elif option == "-h":
            print(texts.menu())

    except IndexError:
        print(texts.menu())
