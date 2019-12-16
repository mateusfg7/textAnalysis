from translate.traduzir import traduzir

def analise_de_sentimento(client, sentenca):
    input = {"sentence": traduzir('en', sentenca)}
    algo = client.algo('nlp/SocialSentimentAnalysis/0.1.4')
    retorno = algo.pipe(input).result
    print("Positivo: {}\nNegativo: {}\nNeutro: {}".format(retorno[0]['positive'], retorno[0]['negative'], retorno[0]['neutral']))