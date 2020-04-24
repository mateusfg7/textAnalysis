def checkInternetConnection(request: "function") -> bool:
    try:
        request('https://algorithmia.com/')
        return True
    except:
        return False
