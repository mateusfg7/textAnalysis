import sys
from interface.texts import optionsTitle


def frequencyOfWords(client, texto):
    print(optionsTitle('--frequency'))
    arguments = sys.argv
    file = arguments[arguments.index('--file') + 1]

    try:
        wordCount = arguments[arguments.index('--frequency') + 1]
    except:
        print("Você não indicou o número de palavras analisadas!")
        print(
            f"analysis.py --file {file} --frequency [numero de palavras analisadas]")
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
