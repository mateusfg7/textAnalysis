import math

from translate.traduzir import traduzir

def analise_de_sentimento(client, sentenca):
    input = {"sentence": traduzir('en', sentenca)}
    
    algo = client.algo('nlp/SocialSentimentAnalysis/0.1.4')
    retorno = algo.pipe(input).result

    positivo = math.floor(retorno[0]['positive'] * 100)
    negativo = math.floor(retorno[0]['negative'] * 100)
    neutro = math.floor(retorno[0]['neutral'] * 100)

    print("Positivo: {}%\nNegativo: {}%\nNeutro: {}%".format(positivo, negativo, neutro))