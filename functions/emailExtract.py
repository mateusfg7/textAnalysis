from interface.texts import optionsTitle


def emailExtract(client, text):
    print(optionsTitle('--email'))
    algo = client.algo('cindyxiaoxiaoli/EmailExtractor/0.2.0')
    response = algo.pipe(text).result
    if len(response) >= 0:
        print(f'foram encontrados {len(response)} emails:\n')
        for item in response:
            print(f'{item}')
