from typing import Callable, NoReturn


def checkInternetConnection(request: Callable[[str], NoReturn]) -> bool:
    '''
    This function needs function param request\n
    example:\n
    import request\n
    checkInternetConnection(request.get)\n
    \n
    return True, if internet connection be ok, or False, if internet connection not be ok.
    '''
    try:
        request('https://algorithmia.com/')
        return True
    except:
        return False
