'''Si el modulo esta dentro de la misma carpeta del .py main se llama directamente
import LlamarModulo.Llamada1

Pero, si esta fuera de la carpeta, osea un nivel anterior debemos:
'''

#Llamar modulos fuera de la carpeta

#Importar sys que es una libreria de python que permite acceder a variables y funciones del interprete de python


import sys
'''print(sys.builtin_module_names)''' #Imprime todos los modulos que estan disponibles en el interprete de python, al crear modulos debemos tener en cuenta que los nombres sean diferentes a los nativos de python, ya que si no, python tomara siempre el modulo nativo.


for i,ruta in enumerate(sys.path):
    print(f"{i}: {ruta}") #Esto recorre cada elemento (ruta) y lo imprime en una línea separada e imprime todas las rutas de los modulos que estan disponibles.

#Para agregar una carpeta fuera de la actual:
sys.path.append("E:\\Personal\\Cristian\\Estudio\\Multimedia\\Programación\\Python\\Python\\Ejercicios")


print("")
print("La capeta se aparece al final de la lista.")
for i,ruta in enumerate(sys.path):
    print(f"{i}: {ruta}")  

'''from modulo_3 import fecha_hoy''' #PAra que esta manera funcione debemos importar la carpeta con sys.path.append. Esta manera funciona más directa pero el modulo_3 aparece con error ya que no se encuentra en la carpeta actual. Ese error de Pylance no es de ejecución, es de análisis estático del editor, y puede que esté ignorando tu sys.path.append(...)

from Ejercicios.modulo_3 import fecha_hoy #De esta manera accede a la carpeta Ejercicios sin necesidad de importar

print(fecha_hoy())