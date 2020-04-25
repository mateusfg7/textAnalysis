def checkInternetConnection(request) -> bool:
    try:
        request('https://algorithmia.com/')
        return True
    except:
        return False
