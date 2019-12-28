from translate.traduzir import traduzir

def reconhecimento_de_entidades(client, arquivo):
    
    if arquivo:

        texto = traduzir('en', arquivo)
        input = {"document": texto}

        algoritimo = client.algo('StanfordNLP/NamedEntityRecognition/0.2.0')
        resultado = algoritimo.pipe(input).result

        numeroDeEntidadesEncontradas = len(resultado['sentences'])
        wordlist = resultado['sentences'][numeroDeEntidadesEncontradas - 1]['detectedEntities']

        if len(wordlist) == 0:
            print("Não foram encontradas nenhuma entidade.")
            exit()
        else:
            for name in wordlist:
                print('Nome: {} \nEntidade: {}\n'.format(name['word'], traduzir('pt', name['entity']).capitalize()))
    
    else:
        print("Texto em branco.")