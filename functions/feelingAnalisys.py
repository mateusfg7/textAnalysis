import math

from typing import Dict, List

from utils.translate import traduzir
from interface.texts import optionsTitle


def feelingAnalisys(client, sentenca: str) -> None:
    print(optionsTitle('--feeling'))

    text: Dict[str, str] = {"sentence": traduzir('en', sentenca)}

    algoritimo = client.algo('nlp/SocialSentimentAnalysis/0.1.4')
    response: List[dict] = algoritimo.pipe(text).result

    positive: int = math.floor(response[0]['positive'] * 100)
    negative: int = math.floor(response[0]['negative'] * 100)
    neutral: int = math.floor(response[0]['neutral'] * 100)

    print("Positivi: {}%\nNegativo: {}%\nNeutro: {}%".format(
        positive, negative, neutral))
