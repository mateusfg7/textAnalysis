from interface.texts import optionsTitle


def countWords(client, text):
    print(optionsTitle('--count'))
    algoritimo = client.algo('diego/WordCounter/0.1.0')
    print(algoritimo.pipe(text).result)
