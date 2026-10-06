def verificar_vencedor(jogada1, jogada2):

    if jogada1 == jogada2:
        return "Empate"

    if (
        (jogada1 == "pedra" and jogada2 == "tesoura") or
        (jogada1 == "tesoura" and jogada2 == "papel") or
        (jogada1 == "papel" and jogada2 == "pedra")
    ):
        return "Jogador 1 venceu"

    return "Jogador 2 venceu"