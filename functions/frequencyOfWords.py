import sys
from typing import List

from interface.texts import optionsTitle


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

    wordList: List[str, bool] = [
        texto,
        wordCount,
        True,
        True
    ]

    algoritimo = client.algo('WebPredict/WordFrequencies/0.1.0')
    response: List[dict] = algoritimo.pipe(wordList).result

    count: int = 1
    for word in response:
        print(f"{count}ª Palavra mais comum: {word['word']}")
        print(f"Frequência: {word['frequency']}\n")
        count += 1
