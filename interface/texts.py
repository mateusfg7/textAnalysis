def menu() -> str:
    return (
        """
    Use: analysis.py --file [arquivo] [opção]

    --tag  pegar tags apartir de um texto

    --feeling  obter sentimentos negativos, positivos e neutros apartir de um texto

    --summarize  resumir um texto

    --count  contar palavras contidas em um texto

    --entity  reconhecer nomes de entidades

    --frequency calcular a frequência das n palavras mais comuns de um texto
        analysis.py --file [arquivo] --frequency [numero de palavras analisadas]
    """
    )


def moduleNotFoundError(moduleName: str, modulePackage: str) -> str:
    return(
        f"""
    Biblioteca '{moduleName}' não foi encontrada.
    tente: pip3 install {modulePackage}
        """
    )


def optionsTitle(option: str) -> str:
    textOfOptions = {
        '--tag': '\nPegando tags...\n',
        '--feeling': '\nFazendo análise de sentimentos...\n',
        '--summarize': '\nResumindo texto...\n',
        '--count': '\nContando palavras...\n',
        '--entity': '\nExtraindo entidades...\n',
        '--frequency': '\nObtendo frequencia de cada palavra...\n',
        '--email': '\nExtraindo emails no texto...\n'
    }
    return textOfOptions[option]
