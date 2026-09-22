import asyncio
import websockets
import json

clientes = set()
jogadores = {}
jogador = 0
numeroDeJogada = 0
jogada1 = ""
jogada2 = ""
jogador1 = False
jogador2 = False

async def servidor(websocket):
    global jogador
    global jogada1, jogada2
    global jogador1, jogador2
    vitorioso = 0
    perdedor = 0

    jogador = len(clientes) + 1
    clientes.add(websocket)
    jogadores[websocket] = f"jogador {jogador}"
    

    print("Cliente conectado")
    print("Jogadores conectados:", len(clientes))

    mensagem = {
        "jogador": f"jogador {jogador}",
        "tipo": "conexao"
    }

    await websocket.send(json.dumps(mensagem))

    try:
        async for mensagem in websocket:

            dados = json.loads(mensagem)

            if dados.get("tipo") == "jogada":
                if dados.get("jogador") == "jogador 1":
                    jogada1 = dados.get("valor")

                if dados.get("jogador") == "jogador 2":
                    jogada2 = dados.get("valor")

                print("Jogador 1:", jogada1)
                print("Jogador 2:", jogada2)

                if jogada1 != "" and jogada2 != "":

                    if jogada1 == jogada2:
                        resultado = "Empate"
                    elif (
                        (jogada1 == "pedra" and jogada2 == "tesoura") or
                        (jogada1 == "tesoura" and jogada2 == "papel") or
                        (jogada1 == "papel" and jogada2 == "pedra")
                    ):
                        jogador1 = True
                        resultado = "Jogador 1 venceu"

                    else:
                        jogador2 = True
                        resultado = "Jogador 2 venceu"

                    print(resultado)

                    mensagem_resultado = {
                        "tipo": "resultado",
                        "mensagem": resultado
                    }

                    for cliente in clientes:
                        await cliente.send(json.dumps(mensagem_resultado))

                    if jogador1:
                        vitorioso = "jogador 1"
                        perdedor = "jogador 2"

                    elif jogador2:
                        vitorioso = "jogador 2"
                        perdedor = "jogador 1"

                    mensagemVitoria = {
                        "jogador": vitorioso,
                        "tipo": "vitoria",
                        "mensagem": "Você venceu!"
                    }

                    mensagemDerrota = {
                        "jogador": perdedor,
                        "tipo": "derrota",
                        "mensagem": "Você perdeu!"
                    }

                    for cliente in clientes:

                        if jogadores[cliente] == vitorioso:
                            await cliente.send(json.dumps(mensagemVitoria))
                            print(mensagemVitoria)

                        elif jogadores[cliente] == perdedor:
                            await cliente.send(json.dumps(mensagemDerrota))
                            print(mensagemDerrota)

                    jogada1 = ""
                    jogada2 = ""

                    jogador1 = False
                    jogador2 = False
    finally:

        clientes.remove(websocket)
        del jogadores[websocket]
        jogador -= 1

        print("Cliente saiu")
        print("Jogadores Conectados", len(clientes))

async def main():
    async with websockets.serve(servidor, "localhost", 6969):
        print("Servidor WebSocket funcionando")

        await asyncio.Future()
        
asyncio.run(main())