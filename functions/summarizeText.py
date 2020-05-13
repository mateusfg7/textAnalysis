def summarizeText(client, text: str) -> 'NoReturn':
    from utils.translate import traduzir
    from interface import texts

    print(texts.optionsTitle('summarize'))

    translatedText: str = traduzir('en', text)
    algoritimo = client.algo('nlp/Summarizer/0.1.8')
    response: str = algoritimo.pipe(translatedText).result

    print(traduzir('pt', response))
