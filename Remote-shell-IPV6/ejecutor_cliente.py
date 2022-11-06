import socket
import sys
import argparse

def coms(sock):
    msg = input('-->')

    while msg != "bye":
        
        sock.send(msg.encode('ascii'))
        
        msg = sock.recv(1024)

        print('\nRespuesta:\n'  + msg.decode("ascii"))
        msg = input('-->')

    msg = "bye"
    sock.send(msg.encode('ascii'))



parser = argparse.ArgumentParser(description="Ejecutor de cliente")
parser.add_argument('-ho', '--host', type=str, help='Dirección IP o nombre del servidor al que conectarse.')
parser.add_argument('-p', '--port', type=str, help='Número de puerto del servidor.')
args = parser.parse_args()


try:
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM) 
    s6 = socket.socket(socket.AF_INET6, socket.SOCK_STREAM) 

except socket.error:
    print('Failed to create socket')
    sys.exit()


host = args.host
port = int(args.port)

try:
    s.connect((host,port))

except socket.gaierror:
    s6.connect((host,port))
    s = s6

coms(s)
