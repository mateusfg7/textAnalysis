import sys

def frequencia_de_palavras(client, texto):
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