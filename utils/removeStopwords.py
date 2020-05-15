from typing import List


def removeStopwords(text: str, stopwords: List[str]) -> str:
    for stopword in stopwords:
        text = text.replace(stopword, ' ')
    return text
