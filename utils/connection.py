import sys
import requests


def checkInternetConnection() -> bool:
    try:
        requests.get('https://algorithmia.com/')
        return True
    except:
        return False
