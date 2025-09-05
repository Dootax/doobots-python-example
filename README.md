# DooBots - Python - Exemplo

Este repositório contém um exemplo de um script Python que pode ser executado no DooBots.

## Estrutura Mínima

- `main.py`: Deve conter uma função `main` que receba um argumento do tipo `doobots.Request` e retorne `doobots.Response` ou `dict`.
- `requirements.txt`: Arquivo com as dependências do projeto

## Testando Localmente

Como o pacote `doobots` já está nas dependências do projeto, ele fornece um comando `doobots-run` que deve ser executado na raiz do seu projeto.

Ele espera que, na pasta onde foi executado, contenha os arquivos `main.py` e `input.json`, sendo o seu script principal e o arquivo de atributos de entrada para o teste, respectivamente.

### Configurar o VirtualEnv

```shell
python3 -m venv .venv
source .venv/bin/activate
```

### Executar

```shell
doobots-run
```

Saída:

```json
{"greeting": "Ola, Matheus!"}
```