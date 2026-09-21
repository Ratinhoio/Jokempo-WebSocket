import asyncio
import websockets
import json

clientes = set()
jogador = 0
numeroDeJogada = 0

async def servidor(websocket):
    global jogador

    jogador = len(clientes) + 1
    clientes.add(websocket)
    

    print("Cliente conectado")
    print("Jogadores conectados:", len(clientes))

    mensagem = {
        "jogador": f"jogador{jogador}",
        "tipo": "conexao"
    }

    await websocket.send(json.dumps(mensagem))

    try:
        async for mensagem in websocket:

            dados = json.loads(mensagem)

            if dados.get("tipo") == "jogada":
                for cliente in clientes:

                    if cliente != websocket:
                        
                        await cliente.send(dados.get("valor"))

    finally:

        clientes.remove(websocket)

        print("Cliente saiu")
        print("Jogadores Conectados", len(clientes))

async def main():
    async with websockets.serve(servidor, "localhost", 6969):
        print("Servidor WebSocket funcionando")

        await asyncio.Future()
        
asyncio.run(main())