#Creando un archivo de texto en la carpeta raiz del archivo
## Solución 1: Usar `pathlib` (Recomendada)

from pathlib import Path

# Obtener la ruta del directorio donde está el script actual
directorio_actual = Path(__file__).parent

# Crear la ruta completa del archivo
ruta_archivo = directorio_actual / "nombres_y_apellidos.txt"

with open(ruta_archivo, "w") as arch:
    arch.writelines("Los datos son:\n\n")
    [arch.writelines(f"Nombre: {n}\nApellido: {a}\n--------\n") for n,a in zip(nombres,apellidos)]

## Solución 2: Usar `os.path`
import os

# Obtener la ruta del directorio donde está el script
directorio_actual = os.path.dirname(os.path.abspath(__file__))

# Crear la ruta completa del archivo
ruta_archivo = os.path.join(directorio_actual, "nombres_y_apellidos.txt")

with open(ruta_archivo, "w") as arch:
    arch.writelines("Los datos son:\n\n")
    [arch.writelines(f"Nombre: {n}\nApellido: {a}\n--------\n") for n,a in zip(nombres,apellidos)]

## Solución 3: Cambiar el directorio de trabajo
import os
from pathlib import Path

# Cambiar al directorio donde está el script
os.chdir(Path(__file__).parent)

# Ahora tu código original funcionará
with open("nombres_y_apellidos.txt", "w") as arch:
    arch.writelines("Los datos son:\n\n")
    [arch.writelines(f"Nombre: {n}\nApellido: {a}\n--------\n") for n,a in zip(nombres,apellidos)]

## ¿Por qué pasa esto?

'''
Cuando usas solo el nombre del archivo (`"nombres_y_apellidos.txt"`), Python lo crea en el **directorio de trabajo actual** (working directory), que normalmente es desde donde ejecutas el script, no donde está ubicado el archivo.

La **Solución 1 con `pathlib`** es la más moderna y recomendada porque:
- `__file__` te da la ruta del script actual
- `Path(__file__).parent` te da el directorio que contiene el script
- El operador `/` con `pathlib` funciona en cualquier sistema operativo

¡Con cualquiera de estas soluciones el archivo se creará en la carpeta `trabajando_con_archivos`!
'''