import subprocess
import os, sys
import argparse
import time


def func(line, i):
    r, w = os.pipe()
    pid = os.fork()

    if pid == 0:
        os.close(w)
        r = os.fdopen(r)
        linea = r.read()
        time.sleep(i/10)
        print(line[::-1])
        sys.exit(0)
        
    else:
        os.close(r)
        w = os.fdopen(w, 'w')
        w.write("%s" % line)
        w.flush()
        w.close()


def main():

    parser = argparse.ArgumentParser(description="Invertir el orden de las letras de cada linea de texto.")
    parser.add_argument('-f', '--file', help='Path del archivo de texto')
    
    args = parser.parse_args()

    with open(args.file, "r") as file:
        spliter = file.read().split("\n")
        a = 0
        while a != len(spliter):
            func(spliter[a-1], a)
            a += 1

    
if __name__ == '__main__':
    main()
