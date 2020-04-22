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
rangeOfOptions = ['--tag', '--feeling', '--summarize',
                  '--count', '--entity', '--frequency', '--help', '-h']

if len(arguments) > 2:
    found = 0
    for option in rangeOfOptions:
        try:
            ARGUMENT_POSITION = arguments.index(option)
            FILE_ARGUMENT_POSITION = arguments.index('--file')
            choices(option, CLIENT,
                    arguments[FILE_ARGUMENT_POSITION + 1])
            found += 1
        except ValueError:
            pass
    if found == 0:
        print(texts.menu())
        sys.exit()

else:
    print(texts.menu())
    sys.exit()
