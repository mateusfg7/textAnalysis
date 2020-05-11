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


def dependencies(colors: dict, option=None) -> str:
    texts = {
        'verify': f'Verificando dependencias...\n{colors["reset"]}',
        'algorithmiaPass': f'Algorithmia {colors["green"]}OK{colors["reset"]}',
        'algorithmiaError': f'Algorithmia {colors["red"]}NOT FOUND{colors["reset"]}',
    }
    return texts[option]
