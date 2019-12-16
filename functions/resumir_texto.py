from translate.traduzir import traduzir

def resumir_texto(client, texto):
    input = traduzir('en', texto)
    algo = client.algo('nlp/Summarizer/0.1.8')
    resultado = algo.pipe(input).result
    print(traduzir('pt', resultado))