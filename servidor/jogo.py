def verificarGanhador(jogada1, jogada2):
    if jogada1 != "" and jogada2 != "":
    
        if jogada1 == jogada2:
            return "Empate"
        elif (
            (jogada1 == "pedra" and jogada2 == "tesoura") or
            (jogada1 == "tesoura" and jogada2 == "papel") or
            (jogada1 == "papel" and jogada2 == "pedra")
        ):
            return "Jogador 1 venceu"
    
        else:
            return "Jogador 2 venceu"
    else:
        return "Aguardando"
