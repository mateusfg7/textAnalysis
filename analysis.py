import sys

try:
    import Algorithmia
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





def pegar_tags():
    arquivo = sys.argv[2]

    try:
        openFile = open('{}'.format(arquivo), 'r')
    except FileNotFoundError:
        print('Arquivo não encontrado!')
        sys.exit(1)
    
    input = openFile.read()

    client = Algorithmia.client('simC43S79CE5FQyQ35I6X8UWv3z1')
    algo = client.algo('nlp/AutoTag/1.0.1')

    print(algo.pipe(input).result)
    openFile.close



def analise_de_sentimento():
    
    arquivo = sys.argv[2]

    try:
        openFile = open('{}'.format(arquivo), 'r')
    except FileNotFoundError:
        print('Arquivo não encontrado!')
        sys.exit(1)

    sentenca = openFile.read()
    traduzido = translator.translate(sentenca, dest='en')


    input = {
    "sentence": traduzido.text
    }

    client = Algorithmia.client('simC43S79CE5FQyQ35I6X8UWv3z1')
    algo = client.algo('nlp/SocialSentimentAnalysis/0.1.4')
    
    retorno = algo.pipe(input).result

    print("Positivo: {}\nNegativo: {}\nNeutro: {}".format(retorno[0]['positive'], retorno[0]['negative'], retorno[0]['neutral']))
    openFile.close()


def resumir_texto():

    arquivo = sys.argv[2]

    try:
        openFile = open('{}'.format(arquivo), 'r')
    except FileNotFoundError:
        print('Arquivo não encontrado!')
        sys.exit(1)
    
    texto = openFile.read()
    input = translator.translate(texto, dest='en')

    client = Algorithmia.client('simC43S79CE5FQyQ35I6X8UWv3z1')
    algo = client.algo('nlp/Summarizer/0.1.8')
    
    resultado = algo.pipe(input.text).result

    traducao = translator.translate(resultado, dest='pt')
    print(traducao.text)
    openFile.close


def contar_palavras():
    
    arquivo = sys.argv[2]

    try:
        openFile = open('{}'.format(arquivo), 'r')
    except FileNotFoundError:
        print('Arquivo não encontrado!')
        sys.exit(1)

    texto = openFile.read()
    openFile.close
    
    input = texto
    client = Algorithmia.client('simC43S79CE5FQyQ35I6X8UWv3z1')
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