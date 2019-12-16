def contar_palavras(client, arquivo):
    input = arquivo
    algo = client.algo('diego/WordCounter/0.1.0')
    print(algo.pipe(input).result)