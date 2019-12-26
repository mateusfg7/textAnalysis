# Text Analysis  :squirrel:
### _Programa em python que realiza análise em texto usando recursos da API [Algorithmia](https://algorithmia.com)_
[![Gitpod Ready-to-Code](https://img.shields.io/badge/Gitpod-Ready--to--Code-blue?logo=gitpod)](https://gitpod.io/#https://github.com/mateusfg7/textAnalysis)
[![Funções](https://img.shields.io/badge/go%20to-fun%C3%A7%C3%B5es-blueviolet?style=flat)](#funções)
[![Dependencias](https://img.shields.io/badge/go%20to%20-depend%C3%AAncias-success?style=flat)](#dependências)
[![Uso](https://img.shields.io/badge/go%20to-uso-ff69b4?style=flat)](#uso)
---
## Funções:

- Obter tags a partir de um texto.

- Obter grau de sentimentos positivos, negativos e neutros.

- Resumir um texto.

- Obter nomes de entidades presentes no texto.

- Obter a frequência de determinadas palavras em um texto.

## Dependências:

### _Instale usando o arquivo de dependências do Python:_
```
python3 -m pip install -r requirements.txt
```
### **Ou**

### _instale as dependências separadamente:_

**Algorithmia**
```
pip3 install algorithmia
```
**GoogleTrans**
```
pip3 install googletran
```

## Uso

`analysis.py [opção] [arquivo]`

`-t`  pegar tags
    
`-s`  obter sentimentos negativos, positivos e neutros

`-r`  resumir um texto

`-c`  contar palavras

`-e`  reconhecer nomes de entidades

`-f` calcular a frequência das n palavras mais comuns de um texto
(`analysis.py -f [arquivo] [nº de palavras analisadas]`)

**Exêmplos de uso:**

1 - extrair tags em um texto no arquivo 'turing.txt' 

_in:_

```shell
$ python3 analysis.py -t turing.txt
```

_out:_

```shell
['após', 'computação', 'foi', 'para', 'pela', 'química', 'turing', 'uma']
```

2 - pegar a frequência das palavras mais comuns em um texto no arquivo 'turing.txt'

_in:_

```shell
$ python3 analysis.py -f turing.txt 10
```

_out:_

```shell
1ª Palavra: de
Frequência: 21

2ª Palavra: a
Frequência: 10

3ª Palavra: da
Frequência: 10

4ª Palavra: um
Frequência: 10

5ª Palavra: e
Frequência: 8

6ª Palavra: em
Frequência: 8

7ª Palavra: turing
Frequência: 7

8ª Palavra: o
Frequência: 6

9ª Palavra: na
Frequência: 6

10ª Palavra: do
Frequência: 5
```
