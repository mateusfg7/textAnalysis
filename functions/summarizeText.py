from utils.translate import traduzir
from interface.texts import optionsTitle


def summarizeText(client, texto: str) -> None:
    print(optionsTitle('--summarize'))

    translatedText: str = traduzir('en', texto)
    algoritimo = client.algo('nlp/Summarizer/0.1.8')
    response: str = algoritimo.pipe(translatedText).result

    print(traduzir('pt', response))
