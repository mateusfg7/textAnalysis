# Text Analysis :shipit:

### _Programa em python que realiza análise em texto usando recursos da API [Algorithmia](https://algorithmia.com)_

[![CodeFactor](https://www.codefactor.io/repository/github/mateusfg7/textanalysis/badge)](https://www.codefactor.io/repository/github/mateusfg7/textanalysis)

_Index_

1. [Funções](#funções)
2. [Dependências](#dependências)
    - [Arquivo de Dependências](#instale-usando-o-arquivo-de-dependências-do-python)
    - [Dependências Separadas](#instale-as-dependências-separadamente)
3. [Uso](#uso)
    - [Exêmplos de Uso](#exêmplos-de-uso)

---

## Funções:

-   Obter tags a partir de um texto.

-   Obter grau de sentimentos positivos, negativos e neutros.

-   Resumir um texto.

-   Obter nomes de entidades presentes no texto.

-   Obter a frequência de determinadas palavras em um texto.

## Dependências:

### _Instale usando o arquivo de dependências do Python:_

```
python3 -m pip install -r requirements.txt
```

### **Ou**

### _instale as dependências separadamente:_

**Algorithmia**

```
python3 -m pip install algorithmia
```

**GoogleTrans**

```
python3 -m pip install googletran
```

## Uso

`analysis.py --file [arquivo] [opção]`

`--tag` pegar tags

`--feeling` obter sentimentos negativos, positivos e neutros

`--summarize` resumir um texto

`--count` contar palavras

`--entity` reconhecer nomes de entidades

`--frequency` calcular a frequência das n palavras mais comuns de um texto
(`analysis.py --file [arquivo] --frequency [nº de palavras analisadas]`)

#### Exêmplos de uso:

1 - extrair tags em um texto no arquivo 'turing.txt'

_in:_

```shell
$ python3 analysis.py --file turing.txt --tag
```

_out:_

```shell
['após', 'computação', 'foi', 'para', 'pela', 'química', 'turing', 'uma']
```

2 - pegar a frequência das palavras mais comuns em um texto no arquivo 'turing.txt'

_in:_

```shell
$ python3 analysis.py --file turing.txt --frequency 5
```

_out:_

```shell
1ª Palavra mais comum: de
Frequência: 21

2ª Palavra mais comum: a
Frequência: 10

3ª Palavra mais comum: da
Frequência: 10

4ª Palavra mais comum: um
Frequência: 10

5ª Palavra mais comum: e
Frequência: 8
```

---

**BTC**: _13sGVSdDeVH8HVVKUDFNfrm8Q5sV7Q429o_
**ETH**: _0x0A6B9Eeb640A17bA0a0a96D986C66D0c75A39832_
