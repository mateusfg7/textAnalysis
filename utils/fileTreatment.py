import sys


def readFile(file):
    try:
        with open(file, 'r') as openFile:
            return openFile.read()
    except FileNotFoundError:
        return False


def writeFile(name, content):
    with open(name, 'w') as file:
        file.write(content)
        return True
