import sys


def frequencyOfWords(client, texto):
    try:
        wordCount = int(sys.argv[3])
    except IndexError:
        print("Você não indicou o número de palavras analisadas!")
        print(
            "analysis.py -f {} [numero de palavras analisadas]".format(sys.argv[2]))
        sys.exit(1)

    wordList = [
        texto,
        wordCount,
        True,
        True
    ]
    algoritimo = client.algo('WebPredict/WordFrequencies/0.1.0')
    resultado = algoritimo.pipe(wordList).result
    count = 1
    for palavra in resultado:
        print('{}ª Palavra: {}'.format(count, palavra['word']))
        print('Frequência: {}\n'.format(palavra['frequency']))
        count += 1
