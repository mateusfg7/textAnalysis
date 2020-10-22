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
4. [API Key](#conseguir-algorithmia-api-key)
5. [Créditos](#créditos)
6. [Doe](#doe-heart)

---

## Funções:

-   Obter tags a partir de um texto.

-   Obter grau de sentimentos positivos, negativos e neutros.

-   Resumir um texto.

-   Obter nomes de entidades presentes no texto.

-   Obter a frequência de determinadas palavras em um texto.

-   Contar número de palavras em um texto.

-   Extrair emails presente no texto.

-   Extrair datas presente no texto.

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

Ao executar o arquivo `Analysis.py` irá pedir a chave de autenticação da API Algorithia, para cria-la va ate [API Key](#conseguir-algorithmia-api-key).
![](doc/img/add_api_key.png)

Logo após ira pedir oque vc deseja analisar, se é um arquivo de texto ou se é um texto plano (apenas uma fraze a ser passada no próprio terminal)
![](doc/img/file_menu.png)
![](doc/img/pass_file.png)
![](doc/img/plain_text.png)

Depois irá aparecer um menu para escolher qual a função desejada.
![](doc/img/menu.png)

#### Exêmplos de uso:

1 - Opção `2` - extrair tags em um texto no arquivo 'turing.txt'

```shell
['após', 'computação', 'foi', 'para', 'pela', 'química', 'turing', 'uma']
```

2 - Opção `5` - pegar a frequência das palavras mais comuns em um texto no arquivo 'turing.txt'

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

## Conseguir Algorithmia API Key

1. _Entre no site [Algorithmia.com](https://algorithmia.com) e clique em **Try it For Free**_
   ![step1](doc/img/algorithmia/step1.png)

2. _Preencha as informações e crie sua conta_
   ![step2](doc/img/algorithmia/step2.png)
   ![step3](doc/img/algorithmia/step3.png)

3. _Clique no botão **API Keys** e copie a chave gerada automaticamente (**default-key**)_
   ![step4](doc/img/algorithmia/step4.png)
   ![step5](doc/img/algorithmia/step5.png)

4. \_Cole sua api key e clique **enter**
   ![step5](doc/img/add_api_key.png)

> _a api key fica salva em **auth/keys.json**_

## Créditos

-   [nlp](https://algorithmia.com/users/nlp)

    -   [AutoTag](https://algorithmia.com/algorithms/nlp/AutoTag)
    -   [SocialSentimentAnalysis](https://algorithmia.com/algorithms/nlp/SocialSentimentAnalysis)
    -   [Summarizer](https://algorithmia.com/algorithms/nlp/Summarizer)

-   [StanfordNLP](https://algorithmia.com/users/StanfordNLP)

    -   [NamedEntityRecognition](https://algorithmia.com/algorithms/StanfordNLP/NamedEntityRecognition)

-   [WebPredict (Jeff Sanchez) ](https://algorithmia.com/algorithms/WebPredict/)

    -   [WordFrequencies](https://algorithmia.com/algorithms/WebPredict/WordFrequencies)

-   [Diego Oppenheimer](https://algorithmia.com/algorithms/diego)

    -   [WordCounter](https://algorithmia.com/algorithms/diego/WordCounter)

-   [cindyxiaoxiaoli](https://algorithmia.com/users/cindyxiaoxiaoli)

    -   [EmailExtractor](https://algorithmia.com/algorithms/cindyxiaoxiaoli/EmailExtractor)

-   [PetiteProgrammer](https://algorithmia.com/users/PetiteProgrammer)
    -   [DateExtractor](https://algorithmia.com/algorithms/PetiteProgrammer/DateExtractor)

---

<table align="center">
    <tr align="center">
        <td>
            <h3>Doe :heart:</h3>
        </td>
    </tr>
    <tr>
        <td>
            <b title="BTC">Bitcoin</b>: <em title="BTC">bc1qzdr4z8sxhumv68s2l97rj0pjum2tnr745uh8us</em>
            <br/>
            <b title="BCH">Bitcoin Cash</b>: <em title="BCH">qr4glglnc66desgumtjattkxmps999twg50wyd7ymy</em>
            <br/>
            <b title="ETH">Ethereum</b>: <em title="ETH">0x4a576AC4b87e3F22700dd3462e02d863Ce2B8817</em>
            <br/>
            <b title="LTC">Litecoin</b>: <em title="LTC">ltc1qnrdjc633fx03r98gazjqjeqdz0svs45l9mypfr</em>
            <br/>
            <b title="DASH">Dash</b>: <em title="DASH">Xp9JFeALHdLr9FNbkE6Na3xMqRRTs75YWx</em>
        </td>
    </tr>
</table>
