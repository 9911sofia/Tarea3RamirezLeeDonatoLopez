import argparse
import time
from tabulate import tabulate
from playsound import playsound  # Se importa la libreria de sonido Playsound
from PIL import Image  # Importa la librería PIL


import Presentador_de_imágenes
import lector_texto
import presentador_de_audio

# presentar_imagen(imagen, escala)
# RepAudio(nombre,repet)
# frecuencia_palabras(filepath)

# 1: Presentador de imagenes
# 2: Presentador de sonido
# 3: Analizador de texto

# Presentador de imagenes


def presentar_imagen(imagen, escala):  # método que presenta la imagen

    t1 = time.time()  # mide el tiempo de inicio
    imagen = Image.open(imagen)  # carga la imagen en la variable imagen

    if escala == "1:1":  # verifica si la escala es 1:1
        imagen.show()  # muestra la imagen
        # otra forma es asiganrle la ruta:
        # ruta = ("C:/Users/Henry/Desktop/" + im)
        # luego se cambia la línea im = Image.open(im) por: im = Image.open(ruta)

    if escala == "1:2":  # verifica si la escala es 1:2
        a, b = imagen.size  # guarda el tamaño de la imagen
        esc1 = ((a//2), (b//2))  # aplica la escala
        imagen1 = imagen.resize(esc1)  # escala el tamaño de la imagen
        imagen1.save("meca_1.jpg")  # guarda la imagen como un archivo nuevo
        imagen1.show()

    if escala == "2:1":  # verifica si la escala es 2:1
        a, b = imagen.size
        esc2 = ((a*2), (b*2))
        imagen2 = imagen.resize(esc2)
        imagen2.save("meca_2.jpg")
        imagen2.show()

    t2 = time.time()  # mide el tiempo final
    print('Tiempo del proceso: ', t2 - t1, 'Segundos')  # muestra el tiempo requerido


# Presentador de audio

def RepAudio(nombre,repet):  # Se define una funcion con 2 argumentos de entrada
    for i in range(repet):  # En un rango determinado por el segundo argumento de la funcion
        mp3 = (nombre+ ".mp3")  # Se le asigna a una variable el arcivo mp3 a reproducirse
        playsound(mp3)  # Se reproduce el archivo mp3
        time.sleep(0.5)  # Se espera 0.5 segundos al terminar


# Analizador de texto
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

    file2 = open("Resultados.txt", "w")  # Se abre el txt de resultados para escribir dentro de él
    for key in list(d.keys()):  # El key accede a los elementos y su cantidad en el diccionario creado
        table.append(tuple((key, d[key])))  # Ingresa cada palabra y su cantidad a la lista
    # Los resultados se escriben en el archivo de texto de resultados
    file2.write(tabulate(table, headers=["Palabra", "Cantidad"]))  # Con tabulate se crea una tabla con la lista table
    file2.close()  # Se cierra el txt de los resultados
    end = time.time()


# Argparse

parser = argparse.ArgumentParser(description = 'Tarea 3: Microcontroldadores y microprocesadores.')

parser.add_argument('-m', '--metodo', type=int, help='Metodo a utilizar: 1. Presentador de imagenes, 2. Analizador de texto, 3. Presentador de audio')
parser.add_rgument('-pf', '--filepath', type=str, help='Dirección del archivo.')
parser.add_rgument('-e', '--escala', type=int , help='Escala para el presentador de imagenes.')
parser.add_argument('-r', '--repeticiones', type=int, help='Cantidad de repeticiones del audio')
# rser.add_argument('-t', '--time', action=print(time)


args = parser.parse_args()

#if args.metodo == 1:
#        presentar_imagen(args.filepath, args.escala)
#        if args.





