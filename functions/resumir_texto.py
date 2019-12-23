from translate.traduzir import traduzir

def resumir_texto(client, texto):
    input = traduzir('en', texto)
    algoritimo = client.algo('nlp/Summarizer/0.1.8')
    resultado = algoritimo.pipe(input).result
    print(traduzir('pt', resultado))