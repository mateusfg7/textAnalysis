import requests

def checkInternetConnection():
    try:
        requests.get('https://algorithmia.com/')
        return True
    except:
        return False

def internetFailWarning():
    print("Você não tem conexão com a internet.")
    print("Esse algorítimo precisa de conexão com a internet para ser executado.")
    exit()