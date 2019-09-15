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



def ler_arquivo():
    arquivo = sys.argv[2]
    
    try:
        openFile = open('{}'.format(arquivo), 'r')
        openFile.close
    except FileNotFoundError:
        print('Arquivo não encontrado!')
        sys.exit(1)
    
    return openFile.read()



def pegar_tags():    
    input = ler_arquivo()
    algo = client.algo('nlp/AutoTag/1.0.1')
    print(algo.pipe(input).result)


def analise_de_sentimento():
    sentenca = ler_arquivo()
    traduzido = translator.translate(sentenca, dest='en')

    input = {
    "sentence": traduzido.text
    }

    algo = client.algo('nlp/SocialSentimentAnalysis/0.1.4')
    retorno = algo.pipe(input).result

    print("Positivo: {}\nNegativo: {}\nNeutro: {}".format(retorno[0]['positive'], retorno[0]['negative'], retorno[0]['neutral']))


def resumir_texto():
    texto = ler_arquivo()
    input = translator.translate(texto, dest='en')

    algo = client.algo('nlp/Summarizer/0.1.8')
    resultado = algo.pipe(input.text).result
    traducao = translator.translate(resultado, dest='pt')
    
    print(traducao.text)


def contar_palavras():
    input = ler_arquivo()
    algo = client.algo('diego/WordCounter/0.1.0')
    print(algo.pipe(input).result)



# MAIN
if sys.argv[1] == "-t" :
    pegar_tags()
elif sys.argv[1] == "-s" :
    analise_de_sentimento()
elif sys.argv[1] == "-r":
    resumir_texto()
elif sys.argv[1] == "-c":
    contar_palavras()
else:
    print("""
    Use: analysis.py [opção] [arquivo]

    -t  pegar tags apartir de um texto
    
    -s  obter sentimentos negativos, positivos e neutros apartir de um texto

    -r  resumir um texto

    -c  contar palavras contidas em um texto
    """)