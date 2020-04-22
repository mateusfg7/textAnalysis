import math

from translate.traduzir import traduzir


def feelingAnalisys(client, sentenca):
    texto = {"sentence": traduzir('en', sentenca)}

    algoritimo = client.algo('nlp/SocialSentimentAnalysis/0.1.4')
    retorno = algoritimo.pipe(texto).result

    positivo = math.floor(retorno[0]['positive'] * 100)
    negativo = math.floor(retorno[0]['negative'] * 100)
    neutro = math.floor(retorno[0]['neutral'] * 100)

    print("Positivo: {}%\nNegativo: {}%\nNeutro: {}%".format(
        positivo, negativo, neutro))
