import subprocess
from datetime import datetime
import argparse

parser = argparse.ArgumentParser(description="Ejecutar")
parser.add_argument('-c', '--command', type=str, help='Comando a ejecutar')
parser.add_argument('-f', '--output_file', type=str, help='Archivo de destino')
parser.add_argument('-l', '--log_file', type=str, help='Archivo log')
args = parser.parse_args()

comando = subprocess.Popen(args.command, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, universal_newlines=True)
out, err = comando.communicate()

salida = open(args.output_file, "a")
salida.write(out+'\n')
salida.close()

logf = open(args.log_file, "a")
if len(out) > 1:
    logf.write(str(datetime.now())+ ": Ejecutado correctamente"+ "\n")

else:
    logf.write(str(datetime.now()) + ": "+ err)
