from translate.traduzir import traduzir


def summarizeText(client, texto):
    textoTraduzido = traduzir('en', texto)
    algoritimo = client.algo('nlp/Summarizer/0.1.8')
    resultado = algoritimo.pipe(textoTraduzido).result
    print(traduzir('pt', resultado))
