
import socketserver
import multiprocessing
import threading
import argparse
import subprocess
import os
import signal
import socket

def ipv4_socket():
    serversocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    serversocket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)


    print(int(args.port))
    HOST, PORT = "", int(args.port)
    serversocket.bind((HOST, PORT))
    serversocket.listen(5)

    while True:
        global clientsocketv4
        clientsocketv4, addr= serversocket.accept()
        
        if args.concurrence == "p":
            hijo = os.fork()
            if not hijo:
                # hijo
                print("PID Padre ", os.getppid())
                print("PID Hijo ", os.getpid())
                coms(clientsocketv4)

        if args.concurrence == "t":
            server_thread = threading.Thread(target=coms, kwargs={'clientsock': clientsocketv4,})
            server_thread.daemon = True
            server_thread.start()

def ipv6_socket():
    serversocket = socket.socket(socket.AF_INET6, socket.SOCK_STREAM) 
    serversocket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)


    print(int(args.port))
    HOST, PORT = "localhost", int(args.port)
    serversocket.bind((HOST, PORT))
    serversocket.listen(5)

    while True:
        global clientsocketv6
        clientsocketv6, addr= serversocket.accept()
        
        if args.concurrence == "p":
            hijo = os.fork()
            if not hijo:
                # hijo
                print("PID Padre ", os.getppid())
                print("PID Hijo ", os.getpid())
                coms(clientsocketv6)

        if args.concurrence == "t":
            server_thread = threading.Thread(target=coms, kwargs={'clientsock': clientsocketv6,})
            server_thread.daemon = True
            server_thread.start()

def coms(clientsock):
    while True:
        # establish a connection
        data = clientsock.recv(1024)
        if data.decode()[:3] == "bye":
            print("Cliente desconectado")
            break
        proceso = subprocess.Popen([data], stdout=subprocess.PIPE, stderr=subprocess.PIPE, shell=True)
        out, err = proceso.communicate()

        print("Recibido: "+data.decode("ascii"))
        if err == b'':
            msg = str("OK\n").encode() + out
                    
        if out == b'':
            msg = str("ERROR\n").encode() + err

        clientsock.send(msg)


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Ejecutor de cliente")
    parser.add_argument('-p', '--port', type=str, help='Número de puerto del servidor.')
    parser.add_argument('-c', '--concurrence', type=str, help='Generará un nuevo proceso(p) o hilo(t) al recibir conexiones nuevas.')
    args = parser.parse_args()

    
    ipv4_thread = threading.Thread(target=ipv4_socket)
    ipv6_thread = threading.Thread(target=ipv6_socket)
    # ipv4_thread.daemon = True
    ipv4_thread.start()
    ipv6_thread.start()