#Lista: se crea con corchetes. []
    #Ejem: lista = [1, 2, 3, 4, 5]
#Tupla: se crea con parentesis. ()
    #Ejem: tupla = (1, 2, 3, 4, 5)
#Diccionario: dict{} se crea con llaves. {}
    #Se compone de claves y valores. {'clave': 'valor'}
    #Ejemplo: diccionario = {'nombre': "David", 'edad': 34, "ciudad": "Bogotá"}
#Conjunto: set{} se crea con llaves. {}
    #Ejemplo: conjunto = {"a", "b", "c", True, 4, 5.5}
    #No puede tener elementos repetidos.
    #No tiene orden.
    #No puede tener elementos mutables.
    #No puede tener elementos no hasheables.


"""Listas list()"""

lista = ["a", "b", "c", True, 4, 5.5] # Las listas se definen con corchetes
print("01.", lista) # 01. ['a', 'b', 'c', True, 4, 5.5]
print("02.", lista[0]) # 02. a
print("03.", lista[5]) # 03. 5.5
# print("04.", lista[0:2]) # 04. ['a', 'b']
# print("05.", lista[2:]) # 05. ['c', True, 4, 5.5]
# print("06.", lista[:4]) # 06. ['a', 'b', 'c', True]
# print("07.", lista[-1]) # 07. 5.5
# print("08.", lista[-4]) # 08. c
# print("09.", lista[-4:]) # 09. ['c', True, 4, 5.5]
# print("10.", lista[:-2]) # 10. ['a', 'b', 'c', True]
# print("11.", lista[::2]) # 01. ['a', 'c', 4]
#_____________________________________________________________________________________
lista[0] = "z" # Cambiamos el valor de la primera posición de la lista
print("Valor 0 actualizado de lista", lista[0])

"""Tuplas (tuple)"""
tupla = ("a", "b", "c", True, 4, 5.5) # Las tuplas se definen con parentesis
print("Tupla 0.", tupla[0]) 

#Diferencias entre listas y tuplas
# Las listas son mutables, podemos cambiar sus valores y se definen con corchetes
# Las tuplas son inmutables, no podemos cambiar sus valores y se definen con parentesis
# Las dos se llaman con corchete

"""Conjunto set()"""

#Para definir un conjunto usamos llaves.
#Se pueden redefinir en general pero no podemos cambiar uno a uno sus elementos.
#No podemos acceder a sus elementos usando indices, para acceder a ellos necesitamos un bucle.
#Sus datos son desordenados.
conjunto = {"a", "b", "c", True, 4, 5.5}

"""Diccionarios dict()"""
#Se definen con llaves y tienen una estructura 'clave': valor
#La clave se puede poner entre comillas simples o dobles.
#Se separan los elementos con comas y se accede a ellos con la clave entre corchetes.
#Recordemos que Python reconoce las minuscualas y mayusculas porque es case sensitive. Nombre != nombre.
Diccionario = {
    'nombre': "David", 
    'edad': 34, 
    "ciudad": "Bogotá"
    } 
print("Nombre: ", Diccionario["nombre"])
print("Ciudad:", Diccionario["ciudad"])
