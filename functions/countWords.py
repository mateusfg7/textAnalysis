from interface.texts import optionsTitle


def countWords(client, arquivo):
    print(optionsTitle('--count'))
    texto = arquivo
    algoritimo = client.algo('diego/WordCounter/0.1.0')
    print(algoritimo.pipe(texto).result)
