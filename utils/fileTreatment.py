import sys

from typing import Optional


def readFile(file: str) -> Optional[str, bool]:
    try:
        with open(file, 'r') as openFile:
            return openFile.read()
    except FileNotFoundError:
        return False


def writeFile(name: str, content: str) -> bool:
    with open(name, 'w') as file:
        file.write(content)
        return True
