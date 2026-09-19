import asyncio
import websockets


clientes = set()    

async def servidor(websocket):

    clientes.add(websocket)
    

    print("Cliente conectado")
    print("Jogadores conectados:", len(clientes))

    try:
        async for mensagem in websocket:

            print("Mensagem recebida:", mensagem)

            for cliente in clientes:

                if cliente != websocket:
                    
                    await cliente.send(mensagem)

    finally:

        clientes.remove(websocket)

        print("Cliente saiu")
        print("Jogadores Conectados", len(clientes))

async def main():
    async with websockets.serve(servidor, "localhost", 6969):
        print("Servidor WebSocket funcionando")

        await asyncio.Future()
        
asyncio.run(main())