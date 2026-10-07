import asyncio
import websockets
import json
from evento import processarJogada, verificarEvento
from sala import clientes, jogadores, adicionarJogador, removerJogador, limparJogadas


lock = asyncio.Lock()


async def servidor(websocket):

    async with lock:

        jogador = adicionarJogador(websocket)

        if jogador is None:
            await websocket.send(json.dumps({
                "tipo": "sala_cheia",
                "mensagem": "Sala cheia. Aguarde a proxima partida."
            }))

            await websocket.close(code=1008, reason="Sala cheia")
            return

        print("Cliente conectado")
        print("Jogadores conectados:", len(clientes))

        mensagem = {
            "jogador": jogador,
            "tipo": "conexao"
        }

    await websocket.send(json.dumps(mensagem))

    try:
        async for mensagem in websocket:

            dados = json.loads(mensagem)

            jogadas = verificarEvento(dados)

            if jogadas is not None:

                jogada1, jogada2 = jogadas

                print("Jogador 1:", jogada1)
                print("Jogador 2:", jogada2)

                mensagens = processarJogada(jogada1, jogada2)

                if mensagens is None:
                    continue

                mensagem1, mensagem2 = mensagens

                for cliente in clientes:

                    if mensagem1.get("tipo") == "empate":
                        await cliente.send(json.dumps(mensagem1))
                        print(mensagem1)

                    elif jogadores[cliente] == mensagem1.get("jogador"):
                        await cliente.send(json.dumps(mensagem1))
                        print(mensagem1)

                    elif jogadores[cliente] == mensagem2.get("jogador"):
                        await cliente.send(json.dumps(mensagem2))
                        print(mensagem2)

                limparJogadas()

    finally:

        removerJogador(websocket)

        print("Cliente saiu")
        print("Jogadores Conectados", len(clientes))


async def main():

    async with websockets.serve(servidor, "localhost", 6969):

        print("Servidor WebSocket funcionando")

        await asyncio.Future()


asyncio.run(main())