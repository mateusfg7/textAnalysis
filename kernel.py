from typing import Callable, Union, NoReturn, Dict


def kernel_start(getClientKey: Callable[['Module'], Union['AlgorithmiaClient', NoReturn]],
                 getTextToAnalyse: Callable[[], Union[str, NoReturn]],
                 texts: Callable[[Dict[str, str]], NoReturn],
                 choices: Callable[[str, 'Client', str], NoReturn],
                 Algorithmia: 'Module',
                 style: Dict[str, str]) -> NoReturn:
    """
        The kernel of algorithm
        """
    CLIENT = getClientKey(Algorithmia)
    TEXT = getTextToAnalyse()

    texts.clearAndShowHeader(style)
    print(texts.choicesMenu(style))
    choice = input('> ')

    texts.clearAndShowHeader(style)
    selectChoice = {
        '1': lambda: choices('tag', CLIENT, TEXT),
        '2': lambda: choices('feeling', CLIENT, TEXT),
        '3': lambda: choices('summarize', CLIENT, TEXT),
        '4': lambda: choices('entity', CLIENT, TEXT),
        '5': lambda: choices('frequency', CLIENT, TEXT),
        '6': lambda: choices('count', CLIENT, TEXT),
        '7': lambda: choices('email', CLIENT, TEXT),
        '8': lambda: choices('date', CLIENT, TEXT)
    }
    selectChoice[choice]()
