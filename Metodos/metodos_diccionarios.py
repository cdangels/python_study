#Recordemos que para crear un diccionario debemos agregar valores dentro de una lista con {}

dict_1 = {
    "Nombre": "Cristian",
    "Edad": 34,
    "Ciudad": "Bogotá"
}
#Tambien se puede escribir en un alinea separando por ,
"""dict_1 = { "Nombre": "Cristian", "Edad": 34, "Ciudad": "Bogotá"}"""

#Iterar un diccionario en Python significa recorrer sus elementos uno por uno para acceder a sus claves, valores o ambos. En Python, los diccionarios se componen de pares clave-valor y se pueden iterar de varias formas según lo que necesites hacer.
#Las claves son los nombres de los elementos del diccionario.
#Los valores son los elementos del diccionario.

"""Keys () -> devuelve las claves"""
keys = dict_1.keys()
print("Método Keys: ", keys)
#Keys al igual que Items nos sirve para iterar el diccionario.

"""get() -> devuelve el valor de una clave"""
#Se crea la variable, (en este caso get), se llama al diccionario (dict_1) con (.get) y el nombre de la clave que se quiere obtener ("Nombre").
get = dict_1.get("Nombre")
print("Método Get: Nombre= ",get)

"""pop() -> elimina un elemento del diccionario"""
#Si quiere eliminar más de un elemento, los separo por comas.
dict_1.pop("Edad")
#dict_1.pop("Edad", "Ciudad")
print("Método Pop: ", dict_1)

"""items() -> para iterar el dict"""
iterar_items = dict_1.items()
print("Método Items: ", iterar_items)
#Con este metodo podemos iterar el diccionario, osea, recorrer sus elementos uno por uno para acceder a sus claves, valores o ambos.

"""clear() -> elimina todos los elementos"""
#No es necesario crear una variable para el método clear, ya que este no devuelve nada
dict_1.clear()
print(dict_1)