import multiprocessing as mp
from multiprocessing import Process, Pool, Queue
import argparse, re, os, math


def txt_to_matrix(file):
    for line in file:
        file.seek(0)
        readf = file.read()
        splitfile1 = readf.split("\n")
        splitfile2 = []
        for i in range(len(splitfile1)-1):
            splitfile2.append(splitfile1[i].split(", "))
        return splitfile2

def raiz(matrix):
    res = []
    print("Process: ", os.getpid(), os.getppid())
    for i in range(len(matrix)):
        num = int(matrix[i])
        res.append(math.sqrt(num))
    return(res)

def pot(matrix):
    res = []
    print("Process: ", os.getpid(), os.getppid())
    for i in range(len(matrix)):
        num = int(matrix[i])
        res.append(num*num)
    return(res)

def log(matrix):
    res = []
    print("Process: ", os.getpid(), os.getppid())
    for i in range(len(matrix)):
        num = int(matrix[i])
        res.append(math.log(num))
    return(res)


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description="Calculadora de matrices.")
    parser.add_argument('-p', '--cantidad_procesos', help='Cantidad de procesos deseados')
    parser.add_argument('-f', '--file', help='Path del archivo de texto')
    parser.add_argument('-c', '--funcion_calculo', help='Calculo deseado (raiz, por, log)')
    
    args = parser.parse_args()

    operacion = str(args.funcion_calculo)
    mfile = open(args.file, 'r')
    matrix_lst = txt_to_matrix(mfile)
    mfile.close()

    p = Pool(processes=int(args.cantidad_procesos))
    if operacion == "raiz":
        resultado = p.map(raiz, matrix_lst)
    elif operacion == "pot":
        resultado = p.map(pot, matrix_lst)
    elif operacion == "log":
        resultado = p.map(log, matrix_lst)

    resultado_final = ""
    for x in range(len(resultado)):
        for y in range(len(resultado[x])):
            if y == 0:
                resultado_final = resultado_final + str(resultado[x][y])
            else:
                resultado_final = resultado_final + ", " +str(resultado[x][y])
        print(resultado_final)
        resultado_final = ''


    p.close()
    p.join()
