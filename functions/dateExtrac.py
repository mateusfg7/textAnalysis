from typing import NoReturn, List


def dateExtractor(client: 'Client', text: str) -> NoReturn:
    from utils.translate import traduzir
    from interface import texts

    print(texts.optionsTitle('date'))

    translatedText = traduzir('en', text)
    algorithm = client.algo('PetiteProgrammer/DateExtractor/0.1.0')
    response: List[str] = algorithm.pipe(translatedText).result

    if len(response) > 0:
        for date in response:
            print(date)
    else:
        print('Nenhuma data encontrada')
