def checkModules(texts: 'module', style: dict) -> bool:
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

    return True
