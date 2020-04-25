from interface.texts import optionsTitle


def countWords(client, text: str) -> None:
    print(optionsTitle('--count'))

    algoritimo = client.algo('diego/WordCounter/0.1.0')
    response: int = algoritimo.pipe(text).result

    print(response)
