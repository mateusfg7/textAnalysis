def getTags(client, text: str) -> 'NoReturn':
    from typing import List
    from interface import texts

    print(texts.optionsTitle('tag'))

    algoritimo = client.algo('nlp/AutoTag/1.0.1')
    response: List[str] = algoritimo.pipe(text).result

    print(response)
