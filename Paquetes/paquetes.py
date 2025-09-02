'''MÓDULO vs PAQUETE '''

# Un módulo es un archivo .py que contiene funciones, variables o clases reutilizables. Un paquete es una carpeta que agrupa varios módulos y contiene un archivo __init__.py que permite tratarla como un módulo. Los paquetes se usan para organizar proyectos más grandes y estructurar el código en componentes relacionados. Aunque un paquete es técnicamente un módulo, su función principal es agrupar varios módulos juntos. El archivo __init__.py debe estar en la raíz del paquete para que Python lo reconozca como tal.

'''__init__.py''' #Este archivo es necesario para que un directorio sea visto como un paquete y debe estar alojado en la raiz del paquete. En este caso en Paquetes. Python determina que si la carpeta tiene este archivo, se trata de un paquete de modulos.

'''Importar un paquete'''
#Primera manera
import Paquetes.paquete1
word1 = input(f"Cual es tu marca favorita de ropa: ")
palabra1 = Paquetes.paquete1.palabra(word1)
print(palabra1)

#Segunda manera
from Paquetes.paquete2 import palabra 
palabra2 = palabra(input(f"Cual es tu marca de carro favorita: "))
print(palabra2)

# En la primera forma se importa todo el módulo y se usa el nombre completo para llamar la función, lo que da más claridad y control, especialmente si se usan varias funciones del mismo módulo. Además, se crea una variable intermedia para guardar el valor ingresado, lo que permite reutilizarlo. En la segunda forma se importa solo la función y se llama directamente con el input, lo que hace el código más limpio y rápido, pero sin posibilidad de reutilizar el valor ingresado.
