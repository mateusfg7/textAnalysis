from interface.texts import optionsTitle


def getTags(client, arquivo):
    print(optionsTitle('--tag'))
    algoritimo = client.algo('nlp/AutoTag/1.0.1')
    print(algoritimo.pipe(arquivo).result)
