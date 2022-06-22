import subprocess
import os
import argparse
import time


def suma(pid):
    a = int(pid)
    c = 0
    while a != 0:  
        b = a - 1

        if (b%2) == 0:
            c = c + b
        a-=1

    return(c)

def main():
    parser = argparse.ArgumentParser(description="Suma pares PID")
    parser.add_argument('-n', '--numero', type=str, help='Numero de procesos hijo')
    parser.add_argument('-v', '--verbose', action='store_true', help='Activar modo verboso')
    args = parser.parse_args()

    num = int(args.numero)
    children = []

    if args.verbose:
        
        for i in range(num):
            cp = os.fork()
            print("Starting process "+str(os.getpid()))
            
            if cp > 0:
                children.append(cp)

            else:
                print(str(os.getpid())+" - "+ str(os.getppid())+" = "+str(suma(os.getpid())))
                print("Ending process "+str(os.getpid()))
                os._exit(0)
                
        for i, proc in enumerate(children):
            os.waitpid(proc, 0)
        print("Parent process is closing")
        
    else:
        for i in range(num):
            cp = os.fork()
            if cp == 0:
                print(str(os.getpid())+" - "+ str(os.getppid())+" = "+str(suma(os.getpid())))
                os._exit(0)

        


if __name__ == '__main__':
    main()
