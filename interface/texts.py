def optionsTitle(option: str) -> str:
    textOfOptions = {
        'tag': '\nPegando tags...\n',
        'feeling': '\nFazendo análise de sentimentos...\n',
        'summarize': '\nResumindo texto...\n',
        'count': '\nContando palavras...\n',
        'entity': '\nExtraindo entidades...\n',
        'frequency': '\nObtendo frequencia de cada palavra...\n',
        'email': '\nExtraindo emails no texto...\n'
    }
    return textOfOptions[option]


def modules(style: dict, module: str, message: str = False) -> str:
    texts = {
        'verify': f'Verificando dependencias...\n{style["reset"]}',
        'algorithmia': {
            'pass': f'{style["bold"]}Algorithmia {style["green"]}OK{style["reset"]}',
            'error': f'{style["bold"]}Algorithmia {style["red"]}NOT FOUND{style["reset"]}',
            'install': f'install: https://algorithmia.com/developers/clients/python{style["reset"]}'
        },
        'googletrans': {
            'pass': f'{style["bold"]}GoogleTrans {style["green"]}OK{style["reset"]}',
            'error': f'{style["bold"]}GoogleTrans {style["red"]}NOT FOUND{style["reset"]}',
            'install': f'install: https://pypi.org/project/googletrans/{style["reset"]}',
        },
    }
    if message:
        return texts[module][message]

    return texts[module]
