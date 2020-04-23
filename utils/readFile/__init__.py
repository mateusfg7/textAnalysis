import sys


def readFile(file):
    try:
        with open(file, 'r') as openFile:
            return openFile.read()
    except FileNotFoundError:
        return False
