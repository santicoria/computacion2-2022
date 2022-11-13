import socketserver
import argparse
import os
import asyncio
import signal
import socket
import subprocess

async def handle_coms(reader, writer):
    data = await reader.read(100)
    message = data.decode()

    x = 0

    while message[:3] != "bye":
        x += 1

        pending = []
        for i in range(x):
            print(f"Starting task {i}")
            pending.append(asyncio.create_task(shell_command(data)))

        while pending:
            res = await asyncio.gather(*pending)
            pending.pop(0)
            x -= 1
            out = res[0][0]
            err = res[0][1]
        

        print("Recibido: "+data.decode("ascii"))
        if err == b'':
            msg = str("OK\n").encode() + out
                    
        if out == b'':
            msg = str("ERROR\n").encode() + err

        writer.write(msg)
        data = await reader.read(100)
        message = data.decode()

    print("Cliente desconectado")
    writer.write(str("Conexion cerrada").encode())

async def shell_command(data):
    proceso = subprocess.Popen([data], stdout=subprocess.PIPE, stderr=subprocess.PIPE, shell=True)
    out, err = proceso.communicate()

    return out, err

    #print(f"Esperando datos del cliente (durmiendo {asyncio.all_tasks()})")
    # for t in asyncio.all_tasks():
    #     print(f"Tarea: {t}")
    # data = await reader.read(100)
    # message = data.decode()
    # addr = writer.get_extra_info('peername')

    # print(f"Received {message!r} from {addr!r}")
    # print(f"Send: {message!r}")
    # writer.write(data)
    # print("encolando el mayuscula")
    # writer.write(data.upper())
    # print("ejecutando el drain()")
    # await writer.drain()

    # print("Close the connection")
    # writer.close()
    # for t in asyncio.all_tasks():
    #     print(f"Cerrando Tarea: {t}")

async def start_serving():
    server = await asyncio.start_server(
            handle_coms, '0.0.0.0', args.port)
    await server.serve_forever()


async def main():

    loop = asyncio.get_running_loop()
    loop.create_task(start_serving())

#     server = await asyncio.start_server(
#         handle_coms, '0.0.0.0', args.port)

#     addr = server.sockets[0].getsockname()
#     print(f'Serving on {addr} {asyncio.current_task()}')

# #    async with server:
#     # print(f"Tareas:\n{asyncio.all_tasks()}")
#     await server.serve_forever()



if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Ejecutor de servidor")
    parser.add_argument('-p', '--port', type=str, help='Número de puerto del servidor.')
    args = parser.parse_args()

    x = 0

    loop = asyncio.get_event_loop()
    loop.create_task(main())
    loop.run_forever()