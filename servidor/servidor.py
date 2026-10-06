import asyncio
import websockets
import json
from jogo import verificar_vencedor
from sala import clientes, lock, jogadores, registrar_jogada, pegar_jogadas, limpar_jogadas, definir_jogador


jogador1 = False
jogador2 = False        

async def servidor(websocket):
    vitorioso = 0
    perdedor = 0
    async with lock:
        
        jogador = definir_jogador()

        if jogador is None:
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
                    registrar_jogada(dados.get("jogador"), dados.get("valor"))

                    jogada1, jogada2 = pegar_jogadas()

                    print("Jogador 1:", jogada1)
                    print("Jogador 2:", jogada2)

                    if jogada1 != "" and jogada2 != "":

                        resultado = verificar_vencedor(jogada1, jogada2)

                        if resultado == "Jogador 1 venceu":
                            jogador1 = True

                        elif resultado == "Jogador 2 venceu":
                            jogador2 = True

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

                        limpar_jogadas()    

                        jogador1 = False
                        jogador2 = False
    finally:

        clientes.remove(websocket)
        del jogadores[websocket]

        print("Cliente saiu")
        print("Jogadores Conectados", len(clientes))

async def main():
    async with websockets.serve(servidor, "localhost", 6969):
        print("Servidor WebSocket funcionando")

        await asyncio.Future()
        
asyncio.run(main())
