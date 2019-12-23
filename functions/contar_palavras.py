def contar_palavras(client, arquivo):
    input = arquivo
    algoritimo = client.algo('diego/WordCounter/0.1.0')
    print(algoritimo.pipe(input).result)
