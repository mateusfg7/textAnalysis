from typing import Dict, List, NoReturn


def entityRecognition(client: 'Client', text: str) -> NoReturn:
    import sys

    from utils.translate import traduzir
    from interface import texts

    print(texts.optionsTitle('entity'))

    translatedText: str
    baseText: Dict[str, str]
    response: Dict[str, list]
    numberOfEntityFound: int
    wordlist: List[dict]

    if text:

        translatedText = traduzir('en', text)
        baseText = {"document": translatedText}

        algoritimo = client.algo('StanfordNLP/NamedEntityRecognition/0.2.0')
        response = algoritimo.pipe(baseText).result

        numberOfEntityFound = len(response['sentences'])
        wordlist = response['sentences'][numberOfEntityFound -
                                         1]['detectedEntities']

        if not wordlist:
            print("Não foram encontradas nenhuma entidade.")
            sys.exit(1)
        else:
            for name in wordlist:
                print(
                    f'Nome: {name["word"]} \nEntidade: {traduzir("pt", name["entity"]).capitalize()}'
                )

    else:
        print("Texto em branco.")
