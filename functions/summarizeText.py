from utils.translate import traduzir
from interface.texts import optionsTitle


def summarizeText(client, texto):
    print(optionsTitle('--summarize'))
    textoTraduzido = traduzir('en', texto)
    algoritimo = client.algo('nlp/Summarizer/0.1.8')
    resultado = algoritimo.pipe(textoTraduzido).result
    print(traduzir('pt', resultado))
