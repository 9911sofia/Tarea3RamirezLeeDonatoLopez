# Presentador de imágenes.

# Se debe instalar la libreria Pillow (en Windows).
# Para la instalación ejecutar en la terminal el comando "pip install Pillow".


import argparse
from PIL import Image  # Importa la librería PIL
import time  # Importar la librería time


def presentar_imagen(imagen, escala):  # método que presenta la imagen

    t1 = time.time()  # mide el tiempo de inicio
    imagen = Image.open(imagen)  # carga la imagen en la variable imagen

    if escala == "1:1":  # verifica si la escala es 1:1
        imagen.show()  # muestra la imagen

    elif escala == "1:2":  # verifica si la escala es 1:2
        a, b = imagen.size  # guarda el tamaño de la imagen
        esc1 = ((a//2), (b//2))  # aplica la escala
        imagen1 = imagen.resize(esc1)  # escala el tamaño de la imagen
        imagen1.save("meca_1.jpg")  # guarda la imagen como un archivo nuevo
        imagen1.show()

    elif escala == "2:1":  # verifica si la escala es 2:1
        a, b = imagen.size
        esc2 = ((a*2), (b*2))
        imagen2 = imagen.resize(esc2)
        imagen2.save("meca_2.jpg")
        imagen2.show()


    t2 = time.time()  # mide el tiempo final
    resul = t2 - t1
    return resul


parser = argparse.ArgumentParser(description='Presentador de imagen.')

parser.add_argument('FILEPATH', type=str, help='Dirección de la imagen a escalar.')
parser.add_argument('-e', '--escala', type=str, help='Escala a introducir, es un string. Ej: 1:1 o 1:2')
parser.add_argument('-t', '--time', action='store_true', help='Bandera para mostrar el tiempo de ejecución.')

args = parser.parse_args()
tiempo = args.time

if __name__ == '__main__':
    if tiempo:
        print('El tiempo de ejecucion es: ', presentar_imagen(args.FILEPATH, args.escala))
    else:
        presentar_imagen(args.FILEPATH, args.escala)




# presentar_imagen("meca.jpg", "1:1")  # carga la imagen con escala 1:1
# presentar_imagen("meca.jpg", "1:2")  # carga la imagen con escala 1:2
# presentar_imagen("meca.jpg", "2:1")  # carga la imagen con escala 2:1
