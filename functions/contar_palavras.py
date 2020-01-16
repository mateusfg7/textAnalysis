def contar_palavras(client, arquivo):
    texto = arquivo
    algoritimo = client.algo('diego/WordCounter/0.1.0')
    print(algoritimo.pipe(texto).result)
