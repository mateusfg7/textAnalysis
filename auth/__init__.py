from typing import Union, Dict, Callable


def getKey(readFile: Callable[[str], Union[str, bool]],
           str2json: Callable[[str], dict]) -> Union[dict, bool]:
    strKeys: str = readFile('auth/keys.json')

    jsonKeys: Dict[str, str]
    if strKeys:
        jsonKeys = str2json(strKeys)
        return jsonKeys
    else:
        return False


def createKey(key: str, writeFile: Callable[[str, str], bool]) -> bool:
    jsonKeys: str = f'{"{"}\n "api_key": "{key}"\n{"}"}'
    writeFile('auth/keys.json', jsonKeys)
    return True
