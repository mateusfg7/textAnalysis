import sys

from typing import Union


def readFile(file: str) -> Union[str, bool]:
    '''
    return the content of the file, if file exists, or return False if file not exist. 
    '''
    try:
        with open(file, 'r') as openFile:
            return openFile.read()
    except FileNotFoundError:
        return False


def writeFile(name: str, content: str) -> bool:
    with open(name, 'w') as file:
        file.write(content)
        return True
