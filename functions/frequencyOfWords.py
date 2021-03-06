from typing import List, NoReturn


def frequencyOfWords(client: 'Client', text: str) -> NoReturn:
    from matplotlib import pyplot as plt
    import sys

    from interface import texts

    from utils.removeStopwords import removeStopwords

    wordCount: str = input('nº de palavras a ser analisadas\n> ')
    print(texts.optionsTitle('frequency'))

    stopwords = [' a ', ' com ', ' da ', ' de ', ' do ',
                 ' e ', ' ele ', ' em ', ' na ', ' no ',
                 ' o ', ' para ', ' por ', ' que ', ' se ', ' sua ',
                 ' um ', ' uma ', ' os ', ' ao ', ' mais ', ' quando ',
                 ' como ', ' das ', ' vem ', ' ser ', ' foi ',  ' pela ',
                 ' eu ', ' te '
                 ]
    stopwordsWithoutSpace = ['a', 'com', 'da', 'de', 'de',
                             'do', 'e', 'ele', 'em', 'na', 'no',
                             'o', 'para', 'por', 'que', 'se', 'sua',
                             'um', 'uma', 'os', 'ao' 'mais', 'quando',
                             'como', 'das', 'vem', 'ser', 'foi', 'pela',
                             'eu', 'te'
                             ]
    textWithoutStopwords: str = removeStopwords(text, stopwords)

    wordList: List[str, bool] = [
        textWithoutStopwords,
        wordCount,
        True,
        True
    ]

    algoritimo = client.algo('WebPredict/WordFrequencies/0.1.0')
    response: List[dict] = algoritimo.pipe(wordList).result

    responseWithoutStopwords = []
    for wordInfo in response:
        if wordInfo['word'] not in stopwordsWithoutSpace:
            responseWithoutStopwords.append(wordInfo)

    print('Deseja exibir um gráfico com a frequencia de cada palavra? [s/n]')
    graphicChoice = input('> ')

    if graphicChoice == 's':
        wordsData = []
        frequencyData = []

        for word in responseWithoutStopwords:
            wordsData.append(word['word'])
            frequencyData.append(word['frequency'])

        plt.bar(wordsData, frequencyData)
        plt.show()
    else:
        count: int = 1
        for word in responseWithoutStopwords:
            print(f"{count}ª Palavra mais comum: {word['word']}")
            print(f"Frequência: {word['frequency']}\n")
            count += 1
