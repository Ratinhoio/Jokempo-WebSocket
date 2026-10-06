import asyncio

clientes = set()
lock = asyncio.Lock()
jogadores = {}
jogador = 0
jogada1 = ""
jogada2 = ""


def registrar_jogada(jogador, jogada):

    global jogada1, jogada2

    if jogador == "jogador 1":
        jogada1 = jogada

    if jogador == "jogador 2":
        jogada2 = jogada


def pegar_jogadas():

    return jogada1, jogada2


def limpar_jogadas():

    global jogada1, jogada2

    jogada1 = ""
    jogada2 = ""

def definir_jogador():

    global jogador

    if "jogador 1" not in jogadores.values():
        jogador = 1

    elif "jogador 2" not in jogadores.values():
        jogador = 2

    else:
        return None

    return jogador