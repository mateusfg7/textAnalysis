def getTags(client, arquivo):
    algoritimo = client.algo('nlp/AutoTag/1.0.1')
    print(algoritimo.pipe(arquivo).result)
