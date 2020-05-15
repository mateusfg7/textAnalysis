from typing import Callable, NoReturn


def checkInternetConnection(request: Callable[[str], NoReturn]) -> bool:
    try:
        request('https://algorithmia.com/')
        return True
    except:
        return False
