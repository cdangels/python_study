#La iteración de diccionarios funciona diferente a las listas, ya que los diccionarios no tienen índices, por lo que no se pueden recorrer de la misma manera. Para recorrer un diccionario se puede hacer de la siguiente manera:

diccionario = {
    "Nombre": "Cristian",
    "Apellido": "Angel",
    "Edad": 34,
    "Ciudad": "Bogotá",
}

#Al solicitar el diccionario se obtiene un objeto de tipo dict_keys, que es un objeto iterable con las claves del diccionario.
print("Claves del diccionario")
for datos in diccionario:
    print(datos)

print()
#Al agregar .items en el diccionario nos devuelve una tupla con los items del diccionario
print("Tupla con claves y valores del diccionario")
for datos in diccionario.items():
    print(datos)

print()
#Para acceder por separado a las claves y los valores usamos la siguiente sintaxis:
print("Acceder por separado a las claves y los valores")
for datos in diccionario.items():
    key = datos[0]
    value = datos[1]
    print(f"Clave: {key}, Valor: {value}")
    
#De esta manera estamos recorriendo un diccionario y accediendo a sus claves y valores.
#Si se quiere acceder a los valores directamente, se puede hacer de la siguiente manera:
print()
