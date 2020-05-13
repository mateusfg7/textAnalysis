def countWords(client, text: str) -> 'NoReturn':
    from interface import texts

    print(texts.optionsTitle('count'))

    algoritimo = client.algo('diego/WordCounter/0.1.0')
    response: int = algoritimo.pipe(text).result

    print(response)
