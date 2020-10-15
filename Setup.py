# pip install twine
# Comando para istalar twine


from setuptools import setup, find_packages
import pathlib

here = pathlib.Path(__file__).parent.resolve()


setup(
    # Con esta linea se instala el programa
    # $ pip3 install git+https://github.com/9911sofia/Tarea3RamirezLeeDonatoLopez

    name='Tarea3RamirezLeeDonatoLopez',  # Nombre del proyecto

    version='1.0',  # Required

    url='https://github.com/9911sofia/Tarea3RamirezLeeDonatoLopez',  # Enlace al proyecto

    author='RamirezLeeDonatoLopez',

    packages=find_packages(where='src'),  # Required

    py_modules=["Presentador_de_imágenes", "lector_texto", "presentador_de_audio"],

    install_requires=['Pillow', 'tabulate', 'playsound'],

    python_requires='~=3.3',


    # package_data={  # Optional
    #     'sample': ['package_data.dat'],
    # },

    entry_points={  # Optional
        'console_scripts': [
            'texto=sample:lector_texto',
            'audio=sample:presentador_de_audio',
            'imagen=sample:Presentador_de_imágenes',
        ],
    },

)
