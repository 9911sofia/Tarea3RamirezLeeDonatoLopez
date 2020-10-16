# Se debe instalar tabulate para correr este programa. Puede ser con pip install tabulate


import argparse
import time
from tabulate import tabulate

d = dict()  # Crea un diccionario vacío
table = []  # Se crea una lista para meter los resultados de los keys


def frecuencia_palabras(filepath):
    file1 = open(filepath, "r")  # Abre el txt para ser leído
    start = time.time()
    for line in file1:
        line = line.strip().lower()  # Borra cualquier espacio en blanco y mayúscula
        line = line.replace("_", " ")  # Borra el _ que separa las palabras
        words = line.split(" ")  # Divide la línea en palabras

        for word in words:  # Iterate over each word in line
            if word in d:  # Revisa si la palabra es repetida
                d[word] = d[word] + 1  # Si lo es, incrementa el contador de la palabra
            else:
                d[word] = 1  # Si no está, agrega la palabra y el #1 al diccionario

    file2 = open("Resultados.txt", "w+")  # Se abre el txt de resultados para escribir dentro de él
    for key in list(d.keys()):  # El key accede a los elementos y su cantidad en el diccionario creado
        table.append(tuple((key, d[key])))  # Ingresa cada palabra y su cantidad a la lista
    # Los resultados se escriben en el archivo de texto de resultados
    file2.write(tabulate(table, headers=["Palabra", "Cantidad"]))  # Con tabulate se crea una tabla con la lista table
    file2.close()  # Se cierra el txt de los resultados
    end = time.time()
    resul = end - start
    return resul



parser = argparse.ArgumentParser(description='Analizador de texto.')

parser.add_argument('FILEPATH', type=str, help='Dirección del archivo a analizar.')
parser.add_argument('-t', '--time', action='store_true', help='Bandera para mostrar el tiempo de ejecución.')


args = parser.parse_args()
tiempo = args.time

if __name__ == '__main__':
    if tiempo:
        print('El tiempo de ejecucion es: ', frecuencia_palabras(args.FILEPATH))
    else:
        frecuencia_palabras(FILEPATH)


# frecuencia_palabras("Texto_ejemplo.txt")
