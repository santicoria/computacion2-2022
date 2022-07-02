import os, sys, argparse, mmap, signal, time
import multiprocessing as mp
from multiprocessing import Process, Pipe

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

def read(w,q):
    sys.stdin = open(0)
    print("Ingrese una linea: ")
    c = sys.stdin.readline()
    print("La linea ingresada es: %sEncriptando...\n" % c)
    w.send(c)
    w.close()
    while q:
        try:
            print("La linea encriptada es:", q.get())
            break
        except:
            print("Cola vacia... saliendo")
            break

def write(r,q):
    msj = r.recv()
    codec = rot13(msj[:-1])
    r.close()
    q.put(codec)


if __name__ == '__main__':
    r, w = Pipe()

    q = mp.Queue()

    p1 = Process(target=read, args=(w,q))
    p2 = Process(target=write, args=(r,q))

    p1.start()
    p2.start()

    p1.join()
    p2.join()

