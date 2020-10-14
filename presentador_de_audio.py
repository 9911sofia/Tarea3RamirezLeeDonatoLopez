# Programa reproductor ded audio
# Luis Carlos Donato 2017094203

# Para la utilizacion de este programa se necesita la instalacion de la libreria playsound
# Se utiliza el comando "pip install playsound" en la terminal


from playsound import playsound  # Se importa la libreria de sonido Playsound
import time  # Se importa la libreria de tiempo time


def RepAudio(nombre,repet):  # Se define una funcion con 2 argumentos de entrada
    for i in range(repet):  # En un rango determinado por el segundo argumento de la funcion
        mp3 = (nombre+ ".mp3")  # Se le asigna a una variable el arcivo mp3 a reproducirse
        playsound(mp3)  # Se reproduce el archivo mp3
        time.sleep(0.5)  # Se espera 0.5 segundos al terminar


RepAudio("Hello",4)  # Ejemplo de reproduccion del archivo Hello.mp3, 4 veces.
