from typing import List

from interface.texts import optionsTitle


def getTags(client, arquivo: str) -> None:
    print(optionsTitle('--tag'))

    algoritimo = client.algo('nlp/AutoTag/1.0.1')
    response: List[str] = algoritimo.pipe(arquivo).result

    print(response)
