import sys
try:
    import Algorithmia
except ModuleNotFoundError:
    print("Biblioteca 'Algorithmia' não foi encontrada.")
    print("tente: pip install algorithmia")
    sys.exit(1)




def pegar_tags():
    arquivo = sys.argv[2]

    try:
        openFile = open('{}'.format(arquivo), 'r')
    except FileNotFoundError:
        print('Arquivo não encontrado!')
        sys.exit(1)
    
    input = openFile.read()

    client = Algorithmia.client('simC43S79CE5FQyQ35I6X8UWv3z1')
    algo = client.algo('nlp/AutoTag/1.0.1')

    print(algo.pipe(input).result)
    openFile.close




# MAIN
if sys.argv[1] == "-t":
    pegar_tags()
else:
    print("""
    -t  pegar tags apartir de um texto
        analysis.py -t [arquivo]
    """)