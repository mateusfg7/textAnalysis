def getKey(readFile, str2json):
    strKeys = readFile('auth/keyss.json')
    if strKeys:
        jsonKeys = str2json(strKeys)
        return jsonKeys
    else:
        return False
