
import socketserver
import multiprocessing
import threading
import argparse
import subprocess
import os
import signal
import socket


def coms():
    while True:
        # establish a connection
        data = clientsocket.recv(1024)
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

        clientsocket.send(msg)

def threader():
    print(threading.current_thread().name)
    coms()

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Ejecutor de cliente")
    parser.add_argument('-p', '--port', type=str, help='Número de puerto del servidor.')
    parser.add_argument('-c', '--concurrence', type=str, help='Generará un nuevo proceso(p) o hilo(t) al recibir conexiones nuevas.')
    args = parser.parse_args()

    serversocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM) 
    serversocket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

    signal.signal(signal.SIGCHLD, signal.SIG_IGN)


    HOST, PORT = "", int(args.port)
    serversocket.bind((HOST, PORT))
    serversocket.listen(5)

    while True:
        clientsocket, addr = serversocket.accept()

        if args.concurrence == "p":
            hijo = os.fork()
            if not hijo:
                # hijo
                print("PID Padre ", os.getppid())
                print("PID Hijo ", os.getpid())
                coms()

        if args.concurrence == "t":
            server_thread = threading.Thread(target=threader)
            server_thread.daemon = True
            server_thread.start()
