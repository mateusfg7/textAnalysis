def emailExtract(client, text: str) -> 'NoReturn':
    from typing import List
    from interface import texts

    print(texts.optionsTitle('email'))

    algo = client.algo('cindyxiaoxiaoli/EmailExtractor/0.2.0')
    response: List[str] = algo.pipe(text).result

    if len(response) >= 0:
        print(f'foram encontrados {len(response)} emails:\n')
        for item in response:
            print(f'{item}')
