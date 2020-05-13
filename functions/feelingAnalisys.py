def feelingAnalisys(client, text: str) -> 'NoReturn':
    import math
    from typing import Dict, List
    from utils.translate import traduzir
    from interface import texts

    print(texts.optionsTitle('feeling'))

    translatedText: Dict[str, str] = {"sentence": traduzir('en', text)}

    algoritimo = client.algo('nlp/SocialSentimentAnalysis/0.1.4')
    response: List[dict] = algoritimo.pipe(translatedText).result

    positive: int = math.floor(response[0]['positive'] * 100)
    negative: int = math.floor(response[0]['negative'] * 100)
    neutral: int = math.floor(response[0]['neutral'] * 100)

    print("Positivi: {}%\nNegativo: {}%\nNeutro: {}%".format(
        positive, negative, neutral))
