def pegar_tags(client, arquivo):    
    algo = client.algo('nlp/AutoTag/1.0.1')
    print(algo.pipe(arquivo).result)