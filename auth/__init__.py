def getKey(readFile, str2json):
    strKeys = readFile('auth/keys.json')
    if strKeys:
        jsonKeys = str2json(strKeys)
        return jsonKeys
    else:
        return False


def createKey(key, writeFile):
    jsonKeys = f'{"{"}\n "api_key": "{key}"\n{"}"}'
    strKeys = f''
    writeFile('auth/keys.json', jsonKeys)
    return True
