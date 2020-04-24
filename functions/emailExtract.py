def emailExtract(client, text):
    algo = client.algo('cindyxiaoxiaoli/EmailExtractor/0.2.0')
    response = algo.pipe(text).result
    print(response)
