from typing import Dict, Union, NoReturn


def checkModules(texts: 'Module', style: Dict[str, str]) -> Union[bool, NoReturn]:
    import sys

    print(texts.modules(style, 'verify'))
    try:
        import Algorithmia
        print(texts.modules(style, 'algorithmia', 'pass'))
    except ModuleNotFoundError:
        print(texts.modules(style, 'algorithmia', 'error'))
        print(texts.modules(style, 'algorithmia', 'install'))
        sys.exit(1)

    try:
        import googletrans
        print(texts.modules(style, 'googletrans', 'pass'))
    except ModuleNotFoundError:
        print(texts.modules(style, 'googletrans', 'error'))
        print(texts.modules(style, 'googletrans', 'install'))
        sys.exit(1)

    try:
        import matplotlib
        print(texts.modules(style, 'matplotlib', 'pass'))
    except ModuleNotFoundError:
        print(texts.modules(style, 'matplotlib', 'error'))
        print(texts.modules(style, 'matplotlib', 'install'))
        sys.exit(1)

    return True
