import sys

try:
    import Algorithmia
    client = Algorithmia.client('simC43S79CE5FQyQ35I6X8UWv3z1')
except ModuleNotFoundError:
    print("Biblioteca 'Algorithmia' não foi encontrada.")
    print("tente: pip3 install algorithmia")
    sys.exit(1)

try:
    from googletrans import Translator
    translator = Translator()
except ModuleNotFoundError:
    print("Biblioteca 'googletrans' não foi encontrada.")
    print("tente: pip3 install googletrans")
    sys.exit(1)


from functions.pegar_tags import pegar_tags



def traduzir(language, text):
    return translator.translate(text, dest=language).text



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


def analise_de_sentimento():
    sentenca = ler_arquivo()
    input = {"sentence": traduzir('en', sentenca)}
    algo = client.algo('nlp/SocialSentimentAnalysis/0.1.4')
    retorno = algo.pipe(input).result
    print("Positivo: {}\nNegativo: {}\nNeutro: {}".format(retorno[0]['positive'], retorno[0]['negative'], retorno[0]['neutral']))


def resumir_texto():
    texto = ler_arquivo()
    input = traduzir('en', texto)
    algo = client.algo('nlp/Summarizer/0.1.8')
    resultado = algo.pipe(input).result
    print(traduzir('pt', resultado))


def contar_palavras():
    input = ler_arquivo()
    algo = client.algo('diego/WordCounter/0.1.0')
    print(algo.pipe(input).result)

def reconhecimento_de_entidades():
    texto = traduzir('en', ler_arquivo())
    input = {"document": texto}
    algo = client.algo('StanfordNLP/NamedEntityRecognition/0.2.0')
    resultado = algo.pipe(input).result

    numeroDeEntidadesEncontradas = len(resultado['sentences'])
    wordlist = resultado['sentences'][numeroDeEntidadesEncontradas - 1]['detectedEntities']

    if len(wordlist) == 0:
        print("Não foram encontradas nenhuma entidade.")
        sys.exit(1)
    else:
        for name in wordlist:
            print('Nome: {} \nEntidade: {}\n'.format(name['word'], traduzir('pt', name['entity']).capitalize()))

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
    analise_de_sentimento()
elif sys.argv[1] == "-r":
    resumir_texto()
elif sys.argv[1] == "-c":
    contar_palavras()
elif sys.argv[1] == "-e":
    reconhecimento_de_entidades()
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