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
