'''#Los modulos son todos los archivos .py que contienen funciones y variables que pueden ser usadas en otros archivos. Al crear estos modulos se crea la carpeta _pycache_ donde se enceuntran los archivos .pyc que son los archivos compilados de los modulos
- Los modulos se importan con la palabra reservada import
- Existen modulos creados por python (escritos en C), creados por terceros (thirdparty) y los que nosotros creamos (ownmodules).
- Una funcion def ingresa en el código como un metodo, se puede usar en cualquier parte del código.- 
- Siempre que se trabajan con modulos se deben separar las funciones de las variables o diferenciar su nombre, agregando mayusculas, guiones o guiones bajos.'''

import modulos_saludar as m_saludar 
#as sirve para darle un alias al modulo, organizar nuestra lógica y simplificar el nombre.

nombre = input(f"Por favor ingresa tu nombre: ")
saludo = m_saludar.saludar(nombre)
print(saludo)


'''Llamando una funcion especifica dentro de un módulo.'''
#Desde el modulo_saludar importamos las funciones saludar y despedirse
from modulos_saludar import saludar, despedirse as bye
despedida = bye(nombre)
saludo = saludar(nombre)
print(saludo)
print(despedida)

#___ PRIMER CASO ___
#De este modo se llama el modulo "Llamada1" que esta en la carpeta en este caso llamada "LlamarModulo"
from LlamarModulo.Llamada1 import palabra

'''
import LlamarModulo.Llamada1 as LLM
palabra1 = input("Hola, estas llamando una funcion, por favor digita tu palabra: ")
resultado = LLM.Llamada1.palabra(palabra1)
print(resultado)
#Esta es otra manera de llamar la funcion, importando el modulo y llamando la funcion en la variable resultado
'''

palabra1 = input("Hola, estas llamando una funcion, por favor digita tu palabra: ") #Se crea una variable con la palabra ingresada
resultado = palabra(palabra1) #Se crea la variable resultado, llama a la funcion palabra y agrega la variable anterior palabra1
print(resultado) #Se imprime el resultado

#___ SEGUNDO CASO ___
from LlamarModulo.Llamada1 import signo as FunSigno #Se llama la funcion signo y se le da un alias
#signo = FunSigno.signo("Piscis")
signo_ingresado = input("Ingresa tu signo zodiacal: ") #Se crea una variable con el signo ingresado
print(FunSigno(signo_ingresado)) #Se imprime la funcion


# En el primer caso se usa una variable intermedia "resultado" para guardar el input de la función antes de imprimirlo.
# En el segundo caso se llama la función directamente dentro del print(), lo que ahorra una línea de código.
# Ambas formas son válidas, depende si necesitas reutilizar el resultado o mantener el código más compacto.

