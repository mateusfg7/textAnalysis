import sys

from utils.translate import traduzir
from interface.texts import optionsTitle


def entityRecognition(client, text):
    print(optionsTitle('--entity'))

    if text:

        textoTraduzido = traduzir('en', text)
        textoBase = {"document": textoTraduzido}

        algoritimo = client.algo('StanfordNLP/NamedEntityRecognition/0.2.0')
        resultado = algoritimo.pipe(textoBase).result

        numeroDeEntidadesEncontradas = len(resultado['sentences'])
        wordlist = resultado['sentences'][numeroDeEntidadesEncontradas -
                                          1]['detectedEntities']

        if not wordlist:
            print("Não foram encontradas nenhuma entidade.")
            sys.exit(1)
        else:
            for name in wordlist:
                print(
                    f'Nome: {name["word"]} \nEntidade: {traduzir("pt", name["entity"]).capitalize()}\n'
                )

    else:
        print("Texto em branco.")
