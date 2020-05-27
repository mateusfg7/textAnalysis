from typing import List


def removeStopwords(text: str, stopwords: List[str]) -> str:
    '''
    Removes the chosen stopwords in the text then return the text without stopwords.
    '''
    for stopword in stopwords:
        text = text.replace(stopword, ' ')
    return text
