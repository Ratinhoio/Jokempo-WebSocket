# Jokenpo WebSocket

Jogo de Jokenpo desenvolvido em Python e HTML/JavaScript utilizando WebSocket para comunicação em tempo real entre os jogadores.

## Tecnologias utilizadas

* Python
* WebSocket
* HTML
* CSS
* JavaScript
* Biblioteca `websockets` para Python

## Como instalar

### 1. Instalar o Python

É necessário ter o Python instalado no computador.

Para verificar se o Python está instalado:

```bash
python --version
```

### 2. Instalar a biblioteca WebSocket

No terminal, execute:

```bash
pip install websockets
```

## Como executar

### 1. Iniciar o servidor

Abra o terminal na pasta do projeto e execute:

```bash
python servidor.py
```

Se o servidor estiver funcionando corretamente, aparecerá:

```text
Servidor WebSocket funcionando
```

O servidor será executado em:

```text
ws://localhost:6969
```

### 2. Abrir o jogo

Depois de iniciar o servidor, abra o arquivo HTML do cliente em um navegador.

Para iniciar uma partida, é necessário abrir o jogo em duas janelas ou abas do navegador.

O primeiro jogador conectado será identificado como **Jogador 1** e o segundo como **Jogador 2**.

Caso um terceiro jogador tente entrar enquanto houver dois jogadores conectados, a sala será considerada cheia.

## Como jogar

1. Inicie o servidor Python.
2. Abra o arquivo HTML em duas abas ou janelas.
3. Cada jogador receberá sua identificação.
4. Escolha entre:

   * Pedra
   * Papel
   * Tesoura
5. Clique em **Enviar Jogada**.
6. O servidor recebe as duas jogadas e verifica o resultado.
7. O resultado é enviado aos jogadores.

### Regras

* Pedra vence Tesoura.
* Tesoura vence Papel.
* Papel vence Pedra.
* Se os dois jogadores escolherem a mesma opção, ocorre empate.

## Estrutura do projeto

```text
Jokempo-WebSocket/
│
├── servidor/
│   └── servidor.py
│
└── cliente/
    └── index.html
```

## Comunicação

O cliente se conecta ao servidor utilizando WebSocket:

```text
Cliente HTML/JavaScript
        ↓
    WebSocket
        ↓
Servidor Python
        ↓
    WebSocket
        ↓
Cliente HTML/JavaScript
```

As mensagens são enviadas em formato JSON.

Exemplo de uma jogada:

```json
{
    "tipo": "jogada",
    "jogador": "jogador 1",
    "valor": "pedra"
}
```

O servidor processa as jogadas e envia o resultado para os clientes conectados.
