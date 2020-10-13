# Se debe instalar tabulate para correr este programa. Puede ser con pip install tabulate
import time
from tabulate import tabulate

file1 = open("Texto_ejemplo.txt", "r")  # Abre el txt para ser leído
d = dict()  # Crea un diccionario vacío
table = []  # Se crea una lista para meter los resultados de los keys
start = time.time()


def words_frequency(file):
    for line in file:
        line = line.strip().lower()  # Borra cualquier espacio en blanco y mayúscula
        line = line.replace("_", " ")  # Borra el _ que separa las palabras
        words = line.split(" ")  # Divide la línea en palabras

        for word in words:  # Iterate over each word in line
            if word in d:  # Revisa si la palabra es repetida
                d[word] = d[word] + 1  # Si lo es, incrementa el contador de la palabra
            else:
                d[word] = 1  # Si no está, agrega la palabra y el #1 al diccionario


words_frequency(file1)
file2 = open("Resultados.txt", "w")  # Se abre el txt de resultados para escribir dentro de él


def result_writing(file):
    for key in list(d.keys()):  # El key accede a los elementos y su cantidad en el diccionario creado
        table.append(tuple((key, d[key])))  # Ingresa cada palabra y su cantidad a la lista
    # Los resultados se escriben en el archivo de texto de resultados
    file.write(tabulate(table, headers=["Palabra", "Cantidad"]))  # Con tabulate se crea una tabla con la lista table


result_writing(file2)
file2.close()  # Se cierra el txt de los resultados
end = time.time()
