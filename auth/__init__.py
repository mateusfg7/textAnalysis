from typing import Optional, Dict


def getKey(readFile, str2json) -> Optional[dict, bool]:
    strKeys: str = readFile('auth/keys.json')

    jsonKeys: Dict[str, str]
    if strKeys:
        jsonKeys = str2json(strKeys)
        return jsonKeys
    else:
        return False


def createKey(key: str, writeFile) -> bool:
    jsonKeys: str = f'{"{"}\n "api_key": "{key}"\n{"}"}'
    writeFile('auth/keys.json', jsonKeys)
    return True
