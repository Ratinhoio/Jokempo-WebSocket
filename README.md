# Jokenpo WebSocket

Jogo de Jokenpo desenvolvido em Python e HTML/JavaScript usando WebSocket para fazer a comunicação entre os jogadores em tempo real.

## Tecnologias utilizadas

- Python
- HTML
- CSS
- JavaScript
- WebSocket
- Biblioteca `websockets`

## Como instalar

É necessário ter o Python instalado.

Para verificar:

```bash
python --version
```

Depois, instale a biblioteca utilizada pelo servidor:

```bash
pip install websockets
```

## Como executar

Primeiro, abra o terminal na pasta principal do projeto e execute:

```bash
python servidor/servidor.py
```

Se estiver funcionando, aparecerá:

```text
Servidor WebSocket funcionando
```

O servidor utiliza a porta `6969`.

Depois de iniciar o servidor, abra o arquivo:

```text
cliente/index.html
```

em um navegador.

Para jogar, é necessário abrir o jogo em duas abas ou janelas. O primeiro jogador conectado será o Jogador 1 e o segundo será o Jogador 2.

Se um terceiro jogador tentar entrar enquanto já houver dois jogadores, a sala será considerada cheia.

## Como jogar

1. Inicie o servidor.
2. Abra o `index.html` em duas abas ou janelas.
3. Cada jogador recebe sua identificação.
4. Escolha Pedra, Papel ou Tesoura.
5. Clique em "Enviar Jogada".
6. Quando os dois jogadores escolherem, o servidor verifica o resultado.
7. O resultado é enviado para os jogadores.

### Regras

- Pedra vence Tesoura.
- Tesoura vence Papel.
- Papel vence Pedra.
- Duas jogadas iguais resultam em empate.

##