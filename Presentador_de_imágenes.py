# Presentador de imágenes.

# Se debe instalar la libreria Pillow (en Windows).
# Para la instalación ejecutar en la terminal el comando "pip install Pillow".

from PIL import Image  # Importa la librería PIL
import time  # Importar la librería time


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
    print('Tiempo del proceso: ', t2 - t1, 'Segundos')  # muestra el tiempo reauerido


presentar_imagen("meca.jpg", "1:1")  # carga la imagen con escala 1:1
presentar_imagen("meca.jpg", "1:2")  # carga la imagen con escala 1:2
presentar_imagen("meca.jpg", "2:1")  # carga la imagen con escala 2:1
