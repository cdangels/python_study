import os
import sys
from pathlib import Path

'''Usamos snake_case para nombrar variables y funciones. 
Ejemplo: nombre_completo, suma_numeros, etc.'''

'''Notas y comentarios'''
    #Para crear notas en una linea usamos #
    #Para crear comentarios en varias lineas usamos """

"""
este es un comentario 
de varias lineas
"""

'''Línea de código con comentarios internos para explicar cada parámetro y función:'''

#tk.Button(
    #self,  # Se asocia el botón a la ventana o frame actual (self)
    #text=button,  # Texto que se mostrará en el botón
    #width=14,  # Ancho del botón en caracteres


'''type()'''
    # La funcion type(dato) nos permite saber el tipo de dato que estamos usando.
    # Ejemplo:
    # print(type(5)) # <class 'int'>
    # print(type(5.5)) # <class 'float'>
    # print(type("Hola")) # <class 'str'>
    # print(type(True)) # <class 'bool'>
    # print(type([1, 2, 3])) # <class 'list'>
    # print(type((1, 2, 3))) # <class 'tuple'>
    # print(type({1, 2, 3})) # <class 'set'>
    # print(type({"nombre": "David", "edad": 34})) # <class 'dict'>
   # print(type(None)) # <class 'NoneType'>

'''Strings'''
    # Los string se pueden escribir dentro de comillas simples, dobles o triple.'''
    # Ejemplo:
primer_nombre= 'Cristian'
print(primer_nombre)

print(segundo_nombre:= "David")
# := es el operador de asignación de expresiones de Python 3.8

#Las comillas triples se usan para strings multilínea.
Apellido= '''Angel
Sandoval'''
print(Apellido)

    #En una llamada a print, el carácter = solo se utiliza para argumentos con nombre (como sep, end, o file), pero no para asignar un valor a una variable.

'''Espacios en blanco'''
#Para imprimir un espacio en blanco usamos print() sin argumentos.

'''Diferencia entre FUNCIÓN y MÉTODO'''
'''FUNCIÓN'''
    #Una función es un bloque de código que se ejecuta cuando se llama. Puede recibir argumentos y devolver un valor. print(), input(), type(), etc son     funciones. Ejemplo: print("Hola"), input("Ingrese un número"), type(5), etc.
    #No todas las funciones son metodos, pero todos los metodos son funciones.

'''MÉTODO'''
    # Un método es una función que pertenece a un objeto. lower(), upper(), title(), etc son metodos. 
    # Se llama con la notación de punto. Ejemplo: cadena.lower(), cadena.upper(), cadena.title(), etc.
    
    #Los metodos son funciones especifícas de un objeto'''
        #Por ejemplo: los metodos de una cadena son diferentes a los metodos de una lista.

'''OBJETO'''
    #Es una instancia de una clase. Un objeto es una entidad que tiene atributos y comportamientos unicos. Ejemplo: un carro es un objeto, tiene atributos como color, marca, modelo, etc y comportamientos como encender, apagar, acelerar, frenar, etc. Encender no existe por si solo, es un metodo personalizado del objeto carro.

'''print(variable.__len__()) vs print(len(variable))'''
    #Ambas líneas de código devuelven la longitud de variable, pero hay una diferencia importante en cómo se usa cada una:

    #print(variable.__len__())
        # Llama directamente al método especial __len__() de la variable. 
        # Es una forma explícita de obtener la longitud del objeto.
        # No es la forma recomendada en Python, ya que acceder directamente a los métodos especiales y va en contra del principio de encapsulación.'''

    #Print(len(variable))
        # Es la forma estándar y recomendada en Python.
        # Llama a la función incorporada len(), que a su vez invoca el método __len__() del objeto.
        # Es más legible y sigue las mejores prácticas de Python.'''

    #¿Cuál usar?
        #Siempre usa len(variable), ya que es la forma más clara y Pythonic. Acceder directamente a __len__() solo tiene sentido en casos muy específicos, como al redefinir el método en una clase personalizada.'''

    #Pythonic 
'''Es un término que se refiere a escribir código de Python de una manera que sea clara, concisa y legible.'''

    #Clear
"""Usar clear en el terminal nos permite limpiar la pantalla, pero no borra el historial de comandos."""

'''Dir()'''
    # Para conocer lso metodos que tiene una variable se usa la función dir()"""
    # El formato es dir(variable)"""
lista = list([1, 2, 3])
print(dir(lista))

"""Si intentamos en una tupla invertirla, ordenarla o alterar sus elementos de cualquier forma, nos devolverá un error, ya que las tuplas tanto como los conjuntos son inmutables."""

'''Getters'''
    # Un Getter es un método que obtiene el valor de un atributo privado. En Python, los getters se utilizan para acceder a los atributos privados de una clase de forma segura. Los getters son útiles para proteger los datos de la clase y garantizar que no se modifiquen directamente desde fuera de la clase

'''Del'''
    # El operador del se usa para eliminar elementos de una lista o diccionario. También se puede usar para eliminar variables o atributos de un objeto."""


'''Acceder a un módulo en otra carpeta diferente a la actual.'''
# Ruta absoluta al directorio 'Modulos'
base_dir = Path(__file__).resolve().parent.parent
modulos_path = base_dir / "Modulos"

'''Este fragmento usa pathlib, una biblioteca para trabajar con rutas. La variable __file__ representa la ruta del archivo actual (en este caso notas.py). El método resolve() convierte esa ruta en una ruta absoluta, útil para evitar ambigüedades si se ejecuta desde distintos lugares. Luego, parent se usa dos veces para subir dos niveles en el árbol de directorios, es decir, desde el archivo actual hasta el directorio raíz que contiene tanto Varios/ como Modulos/; ese directorio se guarda en base_dir. Después, con base_dir / "Modulos" se construye una nueva ruta que apunta directamente a la carpeta Modulos, utilizando el operador / que pathlib redefine de manera elegante para concatenar rutas. Así, modulos_path contiene la ruta absoluta a la carpeta Modulos, lo cual permite luego agregarla a sys.path y hacer importaciones desde ahí.'''

# Agregar la ruta al sys.path
sys.path.append(str(modulos_path))

# Importar el módulo
from LlamarModulo import Llamada1 # type: ignore
# type: ignore ignora el error.

# Usar la función
print(Llamada1.signo("Piscis"))

'''Mostrar el nombre del módulo'''
print(__name__)

#En Python, __name__ es una variable especial que existe en todos los archivos .py. Su valor depende de cómo se ejecuta el archivo:

# Si ejecutas el archivo directamente (por ejemplo, python archivo.py), entonces __name__ vale '__main__'.
# Si el archivo es importado desde otro archivo, entonces __name__ toma el nombre del archivo (sin .py).

'''Formas de convertir una cadena de texto en una lista y enumerarla'''

#Imprimir sys.path como lista, una línea por elemento:

for ruta in sys.path:
    print(ruta)
    
#También puedes usar enumerate si quieres numerarlos:

for i, ruta in enumerate(sys.path): #Enumerate te permite numerar los elementos de una lista.
    print(f"{i}: {ruta}")