def clearAndShowHeader(style: dict) -> 'NoReturn':
    from random import randint
    from os import system as terminal

    terminal('clear')
    banners = [
        f'''
    {style['blue']}
     w                w      db               8 w                  
    w8ww .d88b Yb dP w8ww   dPYb   8d8b. .d88 8 w d88b Yb  dP d88b 
     8   8.dP'  `8.   8    dPwwYb  8P Y8 8  8 8 8 `Yb.  YbdP  `Yb. 
     Y8P `Y88P dP Yb  Y8P dP    Yb 8   8 `Y88 8 8 Y88P   dP   Y88P 
                                                        dP         
        ''',
        f'''
        {style['red']}
                                             _ _                 
     _               _      /\              | (_)                
    | |_  ____ _   _| |_   /  \  ____   ____| |_  ___ _   _  ___ 
    |  _)/ _  | \ / )  _) / /\ \|  _ \ / _  | | |/___) | | |/___)
    | |_( (/ / ) X (| |__| |__| | | | ( ( | | | |___ | |_| |___ |
     \___)____|_/ \_)\___)______|_| |_|\_||_|_|_(___/ \__  (___/ 
                                                     (____/      
        ''',
        f'''
        {style['liteGreen']}                                                                         
         _                 _     _____                 __   _                    
    (_)_  ____        (_)_  (_____)  _            (__) (_) ____         ____ 
    (___)(____) _   _ (___)(_)___(_)(_)__    ____  (_)  _ (____) _   _ (____)
    (_) (_)_(_)(_)_(_)(_)  (_______)(____)  (____) (_) (_)(_)__ (_) (_)(_)__ 
    (_)_(__)__   (_)  (_)_ (_)   (_)(_) (_)( )_( ) (_) (_) _(__)(_)_(_) _(__)
     (__)(____)(_) (_) (__)(_)   (_)(_) (_) (__)_)(___)(_)(____) (____)(____)
                                                                  __(_)      
                                                                 (___)       
        ''',
        f'''
        {style['liteYellow']}
     dMMMMMMP dMMMMMP dMP dMP dMMMMMMP .aMMMb  dMMMMb  .aMMMb  dMP     dMP .dMMMb  dMP dMP .dMMMb 
       dMP   dMP     dMK.dMP    dMP   dMP"dMP dMP dMP dMP"dMP dMP     amr dMP" VP dMP.dMP dMP" VP 
      dMP   dMMMP   .dMMMK"    dMP   dMMMMMP dMP dMP dMMMMMP dMP     dMP  VMMMb   VMMMMP  VMMMb   
     dMP   dMP     dMP"AMF    dMP   dMP dMP dMP dMP dMP dMP dMP     dMP dP .dMP dA .dMP dP .dMP   
    dMP   dMMMMMP dMP dMP    dMP   dMP dMP dMP dMP dMP dMP dMMMMMP dMP  VMMMP"  VMMMP"  VMMMP"                                                                                                  
        '''

    ]
    print(f'{banners[randint(0,3)]}{style["reset"]}\n')


def choicesMenu(style: dict) -> str:
    return (f'''
Escolha uma função:

{style['bold']}1{style['reset']} < {style['italic']}Obter tags a partir de um texto.{style['reset']}

{style['bold']}2{style['reset']} < {style['italic']}Obter grau de sentimentos positivos, negativos e neutros.{style['reset']}

{style['bold']}3{style['reset']} < {style['italic']}Resumir um texto.{style['reset']}

{style['bold']}4{style['reset']} < {style['italic']}Obter nomes de entidades presentes no texto.{style['reset']}

{style['bold']}5{style['reset']} < {style['italic']}Obter a frequência de determinadas palavras em um texto.{style['reset']}

{style['bold']}6{style['reset']} < {style['italic']}Contar número de palavras em um texto.{style['reset']}

{style['bold']}7{style['reset']} < {style['italic']}Extrair emails presentes no texto.{style['reset']}
    ''')


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
