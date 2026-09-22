import asyncio
import websockets
import json

clientes = set()
jogador = 0
numeroDeJogada = 0
jogada1 = ""
jogada2 = ""

async def servidor(websocket):
    global jogador
    global jogada1, jogada2

    jogador = len(clientes) + 1
    clientes.add(websocket)
    

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
                        resultado = "Jogador 1 venceu"

                    else:
                        resultado = "Jogador 2 venceu"

                    print(resultado)

                    mensagem_resultado = {
                        "tipo": "resultado",
                        "mensagem": resultado
                    }

                    for cliente in clientes:
                        await cliente.send(json.dumps(mensagem_resultado))
                        jogada1 = ""
                        jogada2 = ""

                        
                    
    finally:

        clientes.remove(websocket)
        jogador -= 1

        print("Cliente saiu")
        print("Jogadores Conectados", len(clientes))

async def main():
    async with websockets.serve(servidor, "localhost", 6969):
        print("Servidor WebSocket funcionando")

        await asyncio.Future()
        
asyncio.run(main())