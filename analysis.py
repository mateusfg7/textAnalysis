import sys

from interface import texts

from choice import condicionais

try:
    import Algorithmia
    CLIENT = Algorithmia.client('simC43S79CE5FQyQ35I6X8UWv3z1')
except ModuleNotFoundError:
    print(texts.moduleNotFoundError('Algorithmia', 'algorithmia'))
    sys.exit(1)


try:
    FIRST_ARGUMENT = sys.argv[1]
    SECOND_ARGUMENT = sys.argv[2]
except IndexError:
    print(texts.menu())
    sys.exit()


condicionais(FIRST_ARGUMENT, CLIENT, SECOND_ARGUMENT)
