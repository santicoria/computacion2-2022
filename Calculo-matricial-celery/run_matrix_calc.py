import calculo_matriz
import argparse
import re

def matrix_dec(archivo):
    l = ""
    line = []

    with open(archivo) as f:

        lines = f.readlines()
        for i in lines:
            line.append(i.split(","))

        for i in range(len(line)):
            for j in range(len(line[i])):
                line[i][j] = line[i][j].replace("\n", "")

        return line


def matrix_recon(matrix):
    with open("resultado.txt", "x") as r:
        for i in range(len(matrix)):
            for j in range(len(matrix[i])):
                if j == 0:
                    r.write(str(matrix[i][j]))
                else:
                    r.write(", " + str(matrix[i][j]))
            r.write("\n")




if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Calculadora de matriz con celery")
    parser.add_argument('-f', '--file', type=str, help='Ruta del archivo.')
    parser.add_argument('-c', '--funcion_calculo', type=str, help='Calculo (raiz, pot, log).')
    args = parser.parse_args()

    calc = args.funcion_calculo
    file = args.file
    resulting_matrix = []
    
    line = matrix_dec(file)
    print(line)

    for i in range(len(line)):
        resulting_matrix.append([])
        for j in range(len(line[i])):
            x = line[i][j]

            if calc == "raiz":
                print(calculo_matriz.raiz(int(x)))
                resulting_matrix[i].append(calculo_matriz.raiz(int(x)))
            
            elif calc == "pot":
                print(calculo_matriz.pot(int(x)))
                resulting_matrix[i].append(calculo_matriz.pot(int(x)))
            
            elif calc == "log":
                print(calculo_matriz.log(int(x)))
                resulting_matrix[i].append(calculo_matriz.log(int(x)))
    
    matrix_recon(resulting_matrix)
    print(resulting_matrix)
