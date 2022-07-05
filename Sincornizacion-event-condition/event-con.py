from threading import Condition, Event, Thread
import argparse, threading, sys, multiprocessing, time
from multiprocessing import Queue


def reader(name, event):
    print("HILO %d: Este es el hilo: %s (%d)" % (name, threading.current_thread().name, threading.current_thread().ident))
    time.sleep(0.1)
    print("Ingrese una linea: ")
    for line in sys.stdin:
        if line == "bye\n":
            print("HILO %d cerrando..." % name)
            break
        else:
            c = line
            print("\nLa linea ingresada es: %sEscribiendo en cola\n" % c)
            q.put(c)
            time.sleep(0.1)
            print("Ingrese otra linea: ")
    event.set()
    return

def writer(name, event):
    print("HILO %s: Esperando...\n" % name)
    event.wait()
    for i in range(q.qsize()):
        text = str(q.get())
        with open(args.path_file, "a") as file:
            file.write(text)
    print("HILO %d cerrando..." % name)
    return


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description="Escribir lineas ingresadas en mayusculas en un archivo.")
    parser.add_argument('-f', '--path_file', help='Path del archivo donde ese guardara el texto.')

    args = parser.parse_args()

    file = args.path_file

    condition = Condition()
    event = Event()

    threads = []
    
    q = multiprocessing.Queue()

    x1 = threading.Thread(target=reader, args=(1,event), daemon=True) 
    threads.append(x1)

    x2 = threading.Thread(target=writer, args=(2,event)) 
    threads.append(x2)

    for x in threads:
        x.start()

    for x in threads:
        x.join()

    time.sleep(0.1)
    print("MAIN: cantidad de threads activos: ", threading.active_count())

    for i in threading.enumerate():
        print("Nombre: ", i.name, "(",i.ident,", Vivo?: ",i.is_alive(),", Daemon?:",i.daemon)

    print("Padre terminando")
  