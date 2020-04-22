import sys

from interface import texts

from choice import choices

try:
    import Algorithmia
    CLIENT = Algorithmia.client('simC43S79CE5FQyQ35I6X8UWv3z1')
except ModuleNotFoundError:
    print(texts.moduleNotFoundError('Algorithmia', 'algorithmia'))
    sys.exit(1)


arguments = sys.argv
rangeOfOptions = ['-t', '-s', '-r', '-c', '-e', '-f', '-h']

if len(arguments) > 1:

    for option in rangeOfOptions:
        try:
            ARGUMENT_POSITION = arguments.index(option)
            choices(option, CLIENT,
                    arguments[ARGUMENT_POSITION + 1])
        except ValueError:
            pass

else:
    print(texts.menu())
    sys.exit()
