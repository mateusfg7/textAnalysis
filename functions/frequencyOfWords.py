import sys
from typing import List

from interface.texts import optionsTitle

from utils.removeStopwords import removeStopwords


def frequencyOfWords(client, texto: str) -> None:
    print(optionsTitle('--frequency'))

    arguments: List[str] = sys.argv
    file: str = arguments[arguments.index('--file') + 1]

    try:
        wordCount: str = arguments[arguments.index('--frequency') + 1]
    except:
        print("Você não indicou o número de words analisadas!")
        print(
            f"analysis.py --file {file} --frequency [numero de words analisadas]")
        sys.exit(1)

    stopwords = [' a ', ' com ', ' da ', ' de ', ' do ',
                 ' e ', ' ele ', ' em ', ' na ', ' no ',
                 ' o ', ' para ', ' por ', ' que ', ' se ', ' sua ',
                 ' um ', ' uma ', ' os ', ' ao ', ' mais ', ' quando ',
                 ' como ', ' das ', ' vem ', ' ser ', ' foi ',  ' pela '
                 ]
    stopwordsWithoutSpace = ['a', 'com', 'da', 'de', 'de',
                             'do', 'e', 'ele', 'em', 'na', 'no',
                             'o', 'para', 'por', 'que', 'se', 'sua',
                             'um', 'uma', 'os', 'ao' 'mais', 'quando',
                             'como', 'das', 'vem', 'ser', 'foi', 'pela'
                             ]
    textWithoutStopwords: str = removeStopwords(texto, stopwords)

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

    count: int = 1
    for word in responseWithoutStopwords:
        print(f"{count}ª Palavra mais comum: {word['word']}")
        print(f"Frequência: {word['frequency']}\n")
        count += 1
