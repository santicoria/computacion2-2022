import socket
import sys
import argparse
import asyncio


async def tcp_echo_client():
    reader, writer = await asyncio.open_connection(
        args.host, args.port)

    #print(reader, writer)
    msg = input("\n--> ")
    while msg != "bye":
        print(f'Send: {msg!r}')
        writer.write(msg.encode())
        await writer.drain()

        data = await reader.read(100)
        print("Received: " + data.decode("ascii"))
        msg = input("\n--> ")

    print('Close the connection')
    print(f'Send: {msg!r}')
    writer.write(msg.encode())
    await writer.drain()

    data = await reader.read(100)
    print(f'Received: {data.decode("ascii")!r}')
    writer.close()
    #print(asyncio.current_task())
    await writer.wait_closed()


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Ejecutor de cliente")
    parser.add_argument('-ho', '--host', type=str, help='Dirección IP o nombre del servidor al que conectarse.')
    parser.add_argument('-p', '--port', type=str, help='Número de puerto del servidor.')
    args = parser.parse_args()


    asyncio.run(tcp_echo_client())
