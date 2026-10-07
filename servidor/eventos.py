from jogo import verificarGanhador
from sala import registrarJogada, obterJogadas


def processarJogada(jogada1, jogada2):

    resultado = verificarGanhador(jogada1, jogada2)

    if resultado == "Aguardando":
        return None

    return criarMensagem(resultado)


def criarMensagem(resultado):

    if resultado == "Jogador 1 venceu":

        mensagemVitoria = {
            "jogador": "jogador 1",
            "tipo": "vitoria",
            "mensagem": "Você venceu!"
        }

        mensagemDerrota = {
            "jogador": "jogador 2",
            "tipo": "derrota",
            "mensagem": "Você perdeu!"
        }

        return mensagemVitoria, mensagemDerrota

    elif resultado == "Jogador 2 venceu":

        mensagemVitoria = {
            "jogador": "jogador 2",
            "tipo": "vitoria",
            "mensagem": "Você venceu!"
        }

        mensagemDerrota = {
            "jogador": "jogador 1",
            "tipo": "derrota",
            "mensagem": "Você perdeu!"
        }

        return mensagemVitoria, mensagemDerrota

    elif resultado == "Empate":

        mensagemEmpate = {
            "tipo": "empate",
            "mensagem": "Deu empate pô :<"
        }

        return mensagemEmpate, mensagemEmpate

    return None, None


def verificarEvento(dados):

    if dados.get("tipo") == "jogada":
        jogador = dados.get("jogador")
        valor = dados.get("valor")

        registrarJogada(jogador,valor)

        return obterJogadas()

    return None


def selecionarMensagem(jogador, mensagem1, mensagem2):

    if mensagem1.get("tipo") == "empate":
        return mensagem1

    elif jogador == mensagem1.get("jogador"):
        return mensagem1

    elif jogador == mensagem2.get("jogador"):
        return mensagem2

    return None