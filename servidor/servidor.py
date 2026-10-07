import asyncio
import websockets
import json
from evento import processarJogada, criarMensagem
from sala import clientes, jogadores, adicionarJogador, removerJogador, registrarJogada, obterJogadas, limparJogadas


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

            if dados.get("tipo") == "jogada":
                async with lock:
                    registrarJogada(dados.get("jogador"), dados.get("valor"))
                    jogada1, jogada2 = obterJogadas()
                    

                print("Jogador 1:", jogada1)
                print("Jogador 2:", jogada2)

                resultado = processarJogada(jogada1, jogada2)

                if resultado == "Aguardando":
                    continue

                mensagem1, mensagem2 = criarMensagem(resultado)

                for cliente in clientes:
                    if resultado == "Empate":
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