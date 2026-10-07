clientes = set()
jogadores = {}

jogada1 = ""
jogada2 = ""


def adicionarJogador(websocket):
    if "jogador 1" not in jogadores.values():
        jogadores[websocket] = "jogador 1"
        clientes.add(websocket)
        return "jogador 1"

    elif "jogador 2" not in jogadores.values():
        jogadores[websocket] = "jogador 2"
        clientes.add(websocket)
        return "jogador 2"

    else:
        return None


def removerJogador(websocket):
    clientes.remove(websocket)
    del jogadores[websocket]


def registrarJogada(jogador, jogada):
    global jogada1, jogada2

    if jogador == "jogador 1":
        jogada1 = jogada

    elif jogador == "jogador 2":
        jogada2 = jogada


def obterJogadas():
    return jogada1, jogada2


def limparJogadas():
    global jogada1, jogada2

    jogada1 = ""
    jogada2 = ""