import asyncio
import websockets
import json
from jogo import verificarGanhador

clientes = set()
lock = asyncio.Lock()
jogadores = {}
jogador = 0
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
    async with lock:
        
        if "jogador 1" not in jogadores.values():
            jogador = 1
        elif "jogador 2" not in jogadores.values():
            jogador = 2
        else:
            await websocket.send(json.dumps({
                "tipo": "sala_cheia",
                "mensagem": "Sala cheia. Aguarde a proxima partida."}))
            await websocket.close(code=1008, reason="Sala cheia")
            return
        clientes.add(websocket)
        jogadores[websocket] =f"jogador {jogador}"
        

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
                async with lock:
                    jogador1 = False
                    jogador2 = False
                    empate = False
                    if dados.get("jogador") == "jogador 1":
                        jogada1 = dados.get("valor")

                    if dados.get("jogador") == "jogador 2":
                        jogada2 = dados.get("valor")

                    print("Jogador 1:", jogada1)
                    print("Jogador 2:", jogada2)

                resultado = verificarGanhador(jogada1, jogada2)

                if resultado == "Jogador 1 venceu":
                    jogador1 = True

                elif resultado == "Jogador 2 venceu":
                    jogador2 = True

                elif resultado == "Empate":
                    empate = True

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

                mensagemEmpate = {
                    "tipo": "empate",
                    "mensagem" : "Deu empate pô :<"
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

                    elif empate:
                        await cliente.send(json.dumps(mensagemEmpate))
                        print(mensagemEmpate)

                        jogada1 = ""
                        jogada2 = ""

                        jogador1 = False
                        jogador2 = False
    finally:

        clientes.remove(websocket)
        del jogadores[websocket]
        jogada1 = ""
        jogada2 = ""

        print("Cliente saiu")
        print("Jogadores Conectados", len(clientes))

async def main():
    async with websockets.serve(servidor, "localhost", 6969):
        print("Servidor WebSocket funcionando")

        await asyncio.Future()
        
asyncio.run(main())