import sys

try:
    import Algorithmia
    client = Algorithmia.client('simC43S79CE5FQyQ35I6X8UWv3z1')
except ModuleNotFoundError:
    print("Biblioteca 'Algorithmia' não foi encontrada.")
    print("tente: pip3 install algorithmia")
    sys.exit(1)


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
        exit()


def menu():
    if sys.argv[1] == "-t" :
        pegar_tags(client, ler_arquivo())

    elif sys.argv[1] == "-s" :
        analise_de_sentimento(client, ler_arquivo())

    elif sys.argv[1] == "-r":
        resumir_texto(client, ler_arquivo())

    elif sys.argv[1] == "-c":
        contar_palavras(client, ler_arquivo())

    elif sys.argv[1] == "-e":
        reconhecimento_de_entidades(client, ler_arquivo())

    elif sys.argv[1] == "-f":
        frequencia_de_palavras(client, ler_arquivo())


try:
    menu()
except IndexError:
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