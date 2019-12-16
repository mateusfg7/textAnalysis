import sys

try:
    import Algorithmia
    client = Algorithmia.client('simC43S79CE5FQyQ35I6X8UWv3z1')
except ModuleNotFoundError:
    print("Biblioteca 'Algorithmia' não foi encontrada.")
    print("tente: pip3 install algorithmia")
    sys.exit(1)


from translate.traduzir import traduzir

from functions.pegar_tags import pegar_tags
from functions.analise_de_sentimento import analise_de_sentimento
from functions.resumir_texto import resumir_texto
from functions.contar_palavras import contar_palavras
from functions.reconhecimento_de_entidades import reconhecimento_de_entidades



def ler_arquivo():
    arquivo = sys.argv[2]
    try:
        openFile = open('{}'.format(arquivo), 'r')
        openFile.close
    except FileNotFoundError:
        if arquivo == 'analysis.py0':
            print('Nenhum arquivo foi passado!')
        else:
            print('Arquivo "{}" não encontrado!'.format(arquivo))
        sys.exit(1)
    return openFile.read()

def frequencia_de_palavras():
    texto = ler_arquivo()
    try:
        wordCount = int(sys.argv[3])
    except:
        print("Você não indicou o número de palavras analisadas!")
        print("analysis.py -f {} [numero de palavras analisadas]".format(sys.argv[2]))
        sys.exit(1)
    input = [
        texto,
        wordCount,
        True,
        True
    ]
    algo = client.algo('WebPredict/WordFrequencies/0.1.0')
    resultado = algo.pipe(input).result
    count = 1
    for palavra in resultado:
        print('{}ª Palavra: {}'.format(count, palavra['word']))
        print('Frequência: {}\n'.format(palavra['frequency']))
        count += 1



# MAIN
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
    frequencia_de_palavras()

else:
    print("""
    Use: analysis.py [opção] [arquivo]

    -t  pegar tags apartir de um texto
    
    -s  obter sentimentos negativos, positivos e neutros apartir de um texto

    -r  resumir um texto

    -c  contar palavras contidas em um texto

    -e  reconhecer nomes de entidades

    -f calcular a frequência das n palavras mais comuns de um texto
        analysis.py -f [arquivo] [numero de palavras analisadas]
    """)