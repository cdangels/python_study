'''El profesor no asiste a clase asi que deja a dos encargados:
1 alumno profesor
1 alumino asistente

A) Pedir la edad de lso compañeros que vinieron a clase y ordenar los datos de mayor a menor.
B) El mayor es el profesor y el menor es el asistente
'''
#Pedir la edad de los companeros
'''
#Usando .append agrega un elemento a la lista, primero se crea la lista seguida de .append y luego se agregan los elementos

compañeros = []

total = input("Cuantas personas son en total.")
print(f"Son {total} personas en total.")

for i in range(total):
    nombre = input("Ingrese el nombre de la persona: ") #Pide el nombre
    edad = int(input("ingrese la edad de la persona: ")) #Pide la edad
    compañero = (nombre,edad) #Crea una tupla con los datos
    compañeros.append(compañero) #Agrega los datos de cada compañero a la lista llamada compañeros.

print(f"compañeros son: {compañeros}")
'''


def obtener_compañeros(cantidad):
    compañeros = [] #Crea una lista, las listas no son mutables.
    for i in range(cantidad): #Ciclo for para recorrer la cantidad de personas.
        nombre = input("Ingrese el nombre de la persona: ") #Pide el nombre.
        edad = int(input("ingrese la edad de la persona: ")) #Pide la edad.
        compañero = (nombre,edad) #Crea una tupla con los datos mutables.
        compañeros.append(compañero) #Agrega los datos de cada compañero a la lista llamada compañeros.
    compañeros.sort(key=lambda x:x[1]) #Toma la lista "compañeros" y la ordena con .sort, el key es para indicar que se quiere ordenar por el segundo termino de la tupla que es la edad.
    asistente = compañeros[0][0] #El asistente es el primer elemento de la lista "compañeros", que es una tupla con dos elementos, el primero es el nombre y el segundo es la edad
    profesor = compañeros[-1][0] #Con -1 se accede al ultimo elemento de una lista.
    return asistente,profesor

total = int(input("Cuantas personas son en total."))
asistente, profesor = obtener_compañeros(total) #primero desempaquetamos la tupla con asistente y profesor.
print(f"Son {total} personas en total.")   
print(f"El profesor es {profesor} y el asistente es {asistente}")