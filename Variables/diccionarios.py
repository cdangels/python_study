#Creando un diccionario con dict()
diccionario = dict(
    Nombre = "Cristian",
    Apellido = "Angel",
    Edad = 34,
    Ciudad = "Bogotá",
    Profesion = "Productor de audio",
    Estado_civil = "Soltero"
)

#Otra manera de crear un diccionario es con {}
diccionario2 = {
    "Nombre": "Cristian",
    "Apellido": "Angel",
    "Edad": 34,
    "Ciudad": "Bogotá",
    "Profesion": "Productor de audio",
    "Estado_civil": "Soltero"
}

#La sintaxis {} es más eficiente y directa, ya que evita la llamada de la función adicional que implica dict().

#Las listas no pueden ser claves de un diccionario, pero las tuplas y los conjuntos sí.
#Ejemplo:
#diccionario = {("clave1", "clave2"): "valor1", ("clave3", "clave4"): "valor2"}

print(diccionario)
print(diccionario2)

#Para crear un diccionario solo con claves se debe usar la función dict.fromkeys(). Dentro de los parentesis se abre corchetes para crear una lista con las claves.

diccionario3 = dict.fromkeys(["Nombre", "Apellido", "Edad", "Ciudad", "Profesion", "Estado_civil"])
print(diccionario3)

#Si dentro de lso parentesis no agregamos la lista el diccionario toma el primer valor como clave iterable y el segundo como valor de cada clave.

diccionario4 = dict.fromkeys("ABCD", "Letra")
print(diccionario4)