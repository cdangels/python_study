from pathlib import Path

# Obtener la ruta del directorio donde está el script actual
actual_dir = Path(__file__).parent

# Crear la ruta completa del archivo
ruta_archivo = actual_dir / "nombres_y_apellidos.txt"

'''
Para llamar o crear el archivo directamente desde el la linea sin importar pathlib se usa:
with open("archivos_problemas_resueltos\\nombres_y_apellidos.txt","w") as arch:
#! pero de esta forma debemos camabiar la ruta si movemos el archivo a otro directorio. Por eso es más optimo usar pathlib.
'''

# Listas con nombres y con apellidos
nombres = ["Cristian", "David", "Oscar", "Juan", "Pedro"]
apellidos = ["Gomez", "Lopez", "Perez", "Martinez", "Garcia"]

#registrarlo en el archivo datos.txt
with open(ruta_archivo,"w") as arch:
    arch.writelines("Los datos son:\n\n")
    [arch.writelines(f"Nombre: {n}\nApellido: {a}\n--------\n") for n,a in zip(nombres,apellidos)]
    #De esta manera se crea una lista con el valor en cada vuelta del bucle for
  
'''  
#!De esta forma bucle for y dentro el método writelines 
with open("nombres_y_apellidos.txt","w") as arch:
    arch.writelines("Los datos son:\n\n")
    for n,a in zip(nombres, apellidos):
        arch.writelines(f"Nombre: {n}\n- Apellido: {a}\n")
'''