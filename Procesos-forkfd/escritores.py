import subprocess
import os
import argparse
import time


def main():

    parser = argparse.ArgumentParser(description="Suma pares PID")
    parser.add_argument('-n', '--numero', type=str, help='Numero de procesos hijo')
    parser.add_argument('-r', '--repeat', help='Cantidad de veces que se almacena cada letra')
    parser.add_argument('-f', '--file', help='Path del archivo de texto')
    parser.add_argument('-v', '--verbose', action='store_true', help='Activar modo verboso')
    
    args = parser.parse_args()

    file = open(args.file, 'a')

    for _ in range(int(args.numero)):
        fk = os.fork()

        if fk == 0:
            letra = chr(65 + _)

            for k in range(int(args.repeat)):
                if args.verbose:
                    print('Proceso '+str(os.getpid())+' escribiendo la letra '+str(letra))
                file.write(letra)
                file.flush()
                time.sleep(1)    
                         
            os._exit(0)

    os.wait()
    file.close()

    print("Parent process is closing")

    file = open(args.file)
    print(file.read())
    file.close
        

if __name__ == '__main__':
    main()
