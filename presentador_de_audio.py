# Programa reproductor ded audio
# Luis Carlos Donato 2017094203

# Para la utilizacion de este programa se necesita la instalacion de la libreria playsound
# Se utiliza el comando "pip install playsound" en la terminal

import argparse

from playsound import playsound  # Se importa la libreria de sonido Playsound
import time  # Se importa la libreria de tiempo time


def RepAudio(nombre,repet):  # Se define una funcion con 2 argumentos de entrada
    start = time.time()
    for i in range(repet):  # En un rango determinado por el segundo argumento de la funcion
        mp3 = (nombre+ ".mp3")  # Se le asigna a una variable el arcivo mp3 a reproducirse
        playsound(mp3)  # Se reproduce el archivo mp3
        time.sleep(0.5)  # Se espera 0.5 segundos al terminar

    end = time.time()
    resul = end - start
    return resul


parser = argparse.ArgumentParser(description='Presentador de audio.')

parser.add_argument('FILEPATH', type=str, help='Dirección del archivo a reproducir.')
parser.add_argument('-r', '--repeticiones', type=int, help='Cantidad de repeticiones del audio a reproducir.')
parser.add_argument('-t', '--time', action='store_true', help='Bandera para mostrar el tiempo de ejecución.')

args = parser.parse_args()
tiempo = args.time

if __name__ == '__main__':
    if tiempo:
        print('El tiempo de ejecución es: ', RepAudio(args.FILEPATH, args.repeticiones))
    else:
        RepAudio(args.FILEPATH, args.repeticiones)









# RepAudio("Hello",4)  # Ejemplo de reproduccion del archivo Hello.mp3, 4 veces.
