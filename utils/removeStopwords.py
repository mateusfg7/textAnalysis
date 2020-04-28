def removeStopwords(text, stopwords):
    for stopword in stopwords:
        text = text.replace(stopword, ' ')
    return text
