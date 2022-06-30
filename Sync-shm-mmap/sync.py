import subprocess
import os, sys
import argparse
import mmap
import signal
import time

area = mmap.mmap(-1, 1024)

def enviar_a_padre(nro, frame):
    area.seek(0)
    line = area.readline()
    print("Linea ingresada: ", line.decode())
    os.kill(child2, signal.SIGUSR1)
    #print("Ingrese linea: ")

def a_mayus(nro, frame):
    area.seek(0)
    line = area.readline()
    #print("Linea ingresada en mayuscula: ", line.decode().upper())
    file.write(line.decode().upper())
    file.flush()
    print("Ingrese linea: ")

def end_child2(nro, frame):
    print("Proceso hijo 2 terminado")
    os._exit(0)

def end_parent_child2(nro, frame):
    os.kill(child2, signal.SIGUSR2)
    

def main():

    parser = argparse.ArgumentParser(description="Reescribir a MAYUSCULAS.")
    parser.add_argument('-f', '--file', help='Path del archivo de texto')
    
    args = parser.parse_args()

    global file
    file = open(args.file, 'a')

    signal.signal(signal.SIGUSR1, enviar_a_padre)
    signal.signal(signal.SIGUSR2, end_parent_child2)

    global child1
    child1 = os.fork()

    if child1 == 0:
        print("Ingrese linea: ")
        for line in sys.stdin:
            if line == "bye\n":
                os.kill(os.getppid(), signal.SIGUSR2)
                print("Proceso hijo 1 terminado")
                os._exit(0)
            area.seek(0)
            area.write(line.encode())
            area.seek(0)
            os.kill(os.getppid(), signal.SIGUSR1)
            
    else:
        global child2
        child2 = os.fork()
        if child2 == 0:
            signal.signal(signal.SIGUSR1, a_mayus)
            signal.signal(signal.SIGUSR2, end_child2)

            while True:
                signal.pause()

        else:
            os.waitpid(child1, 0)
            os.waitpid(child2, 0)
            print("Proceso padre terminado")




if __name__ == '__main__':
    main()
