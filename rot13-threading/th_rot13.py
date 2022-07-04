import multiprocessing
import sys
import threading
import time
import os
from multiprocessing import Queue, Pipe


def rot13(entrada):
    out = ""
    abc = "abcdefghijklmnopqrstuvwxyz"
    for letter in entrada:
        ind = abc.find(letter.lower())
        if letter == " ":
            out = out + " "
        else:
            if ind <= 12:
                out = out + abc[ind+13]
            else:
                x = ind - 13
                out = out + abc[x]
    return out


def read_input(name, w):
    print("HILO %d: Este es el hilo: %s (%d)" % (name, threading.current_thread().name, threading.current_thread().ident))
    sys.stdin = open(0)
    print("Ingrese una linea: ")
    c = sys.stdin.readline()
    print("\nLa linea ingresada es: %sEncriptando...\n" % c)
    w.send(c)
    w.close()
    while q:
        try:
            print("La linea encriptada es:", q.get())
            break
        except:
            print("Cola vacia... saliendo")
            break

def rot13_cypher(name, r):
    msj = r.recv()
    msj_encrypted = rot13(msj[:-1])
    r.close()
    q.put(msj_encrypted)
    print("HILO %d: Este es el hilo: %s (%d)" % (name, threading.current_thread().name, threading.current_thread().ident))


if __name__ == '__main__':

    threads = []

    r, w = Pipe()

    q = multiprocessing.Queue()

    x1 = threading.Thread(target=read_input, args=(1, w), daemon=True) 
    threads.append(x1)

    x2 = threading.Thread(target=rot13_cypher, args=(2, r)) 
    threads.append(x2)
    
    for x in threads:
        x.start()

    for x in threads:
        x.join()
  
    # print("MAIN: cantidad de threads activos: ", threading.active_count())

    # for i in threading.enumerate():
    #     print("Nombre: ", i.name, "(",i.ident,", Vivo?: ",i.is_alive(),", Daemon?:",i.daemon)