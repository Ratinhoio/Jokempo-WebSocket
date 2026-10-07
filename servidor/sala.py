clientes = set()
jogadores = {}


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